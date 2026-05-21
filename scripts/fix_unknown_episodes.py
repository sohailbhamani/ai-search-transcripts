#!/usr/bin/env python3
"""
fix_unknown_episodes.py
Renames unknown-* episode dirs to proper YYYY-MM-DD-slug format
using YouTube Data API v3 for metadata.
Usage: doppler run --project moltbot --config dev -- python fix_unknown_episodes.py <repo_dir>
"""
import os
import re
import sys
import time
import requests
from pathlib import Path

_access_token_cache = {"token": None, "expires_at": 0}


def _get_oauth_access_token():
    """Refresh-token -> access-token exchange, cached until ~5s before expiry."""
    refresh = os.environ.get("YOUTUBE_REFRESH_TOKEN", "")
    cid = os.environ.get("YOUTUBE_CLIENT_ID", "")
    cs = os.environ.get("YOUTUBE_CLIENT_SECRET", "")
    if not (refresh and cid and cs):
        return None

    now = time.time()
    if _access_token_cache["token"] and _access_token_cache["expires_at"] - 5 > now:
        return _access_token_cache["token"]

    try:
        r = requests.post(
            "https://oauth2.googleapis.com/token",
            data={
                "client_id": cid,
                "client_secret": cs,
                "refresh_token": refresh,
                "grant_type": "refresh_token",
            },
            timeout=15,
        )
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print(f"  Warning: OAuth token exchange failed: {e}")
        return None

    _access_token_cache["token"] = data["access_token"]
    _access_token_cache["expires_at"] = now + int(data.get("expires_in", 3600))
    return _access_token_cache["token"]


def slugify(title):
    s = title.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    return s[:60]

def get_yt_metadata(video_id, api_key):
    """Get YouTube video metadata via OAuth (preferred) or API key."""
    try:
        url = "https://www.googleapis.com/youtube/v3/videos"
        oauth_token = _get_oauth_access_token()
        if oauth_token:
            params = {"part": "snippet", "id": video_id}
            headers = {"Authorization": f"Bearer {oauth_token}"}
        else:
            params = {"part": "snippet", "id": video_id, "key": api_key}
            headers = {}
        r = requests.get(url, params=params, headers=headers, timeout=10)
        r.raise_for_status()
        items = r.json().get("items", [])
        if not items:
            return None
        snippet = items[0]["snippet"]
        return {
            "title": snippet["title"],
            "publish_date": snippet["publishedAt"][:10],
            "channel": snippet["channelTitle"],
            "tags": snippet.get("tags", []),
        }
    except requests.exceptions.RequestException as e:
        print(f"  SKIP {video_id}: API error - {e}")
        return None
    except Exception as e:
        print(f"  SKIP {video_id}: Unexpected error - {e}")
        return None

def fix_repo(repo_dir, api_key):
    episodes_dir = Path(repo_dir) / "episodes"
    unknowns = sorted([d for d in episodes_dir.iterdir() if d.name.startswith("unknown-")])
    print(f"Found {len(unknowns)} unknown episodes in {repo_dir}")

    for ep_dir in unknowns:
        # Extract video_id from transcript.md
        md = ep_dir / "transcript.md"
        if not md.exists():
            print(f"  SKIP {ep_dir.name} — no transcript.md")
            continue
        content = md.read_text()
        m = re.search(r'video_id:\s*["\']?([A-Za-z0-9_-]{11})', content)
        if not m:
            print(f"  SKIP {ep_dir.name} — no video_id found")
            continue
        video_id = m.group(1)

        meta = get_yt_metadata(video_id, api_key)
        if not meta:
            print(f"  SKIP {video_id} — not found on YouTube")
            continue

        title = meta["title"]
        date = meta["publish_date"]
        slug = slugify(title)
        new_name = f"{date}-{slug}"
        new_dir = episodes_dir / new_name

        # Update frontmatter in transcript.md
        content = re.sub(r'title:\s*"Unknown"', f'title: "{title.replace(chr(34), chr(39))}"', content)
        content = re.sub(r'publish_date:\s*"unknown"', f'publish_date: "{date}"', content)
        content = re.sub(r'author:\s*"[^"]*"', f'author: "{meta["channel"]}"', content)
        md.write_text(content)

        # Rename directory
        if new_dir.exists():
            print(f"  CONFLICT {new_name} already exists, skipping rename")
        else:
            ep_dir.rename(new_dir)
            print(f"  FIXED {ep_dir.name} -> {new_name}")

        time.sleep(0.3)

    print("Done.")

if __name__ == "__main__":
    repo = sys.argv[1] if len(sys.argv) > 1 else "."
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        print("ERROR: YOUTUBE_API_KEY not set")
        sys.exit(1)
    fix_repo(repo, api_key)

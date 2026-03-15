# AI Search Transcripts

YouTube channel: UCIgnGlGkVRhd4qNFcEwLL4A (https://www.youtube.com/@theAIsearch)

AI Search - Exploring the frontiers of artificial intelligence, search technology, and machine learning.

## Stats

- **15 videos** (Jan 30, 2026 - Mar 8, 2026)
- **53 topics**
- Synced twice daily at midnight and noon CST

## Structure

- `episodes/` - Raw transcript files with YAML frontmatter
- `index/` - Processed searchable index by topic
- `index.json` - Full video metadata index
- `scripts/` - Sync and processing scripts

## Sync Schedule

GitHub Actions runs twice daily at midnight and noon CST to sync latest transcripts.

## Usage

```bash
pip install -r requirements.txt
export SUPADATA_API_KEY=your_key
export YOUTUBE_API_KEY=your_key
python scripts/discover.py
python scripts/download.py
python scripts/enrich.py
python scripts/create_index.py
python scripts/build_index.py
```

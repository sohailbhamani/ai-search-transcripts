---
title: "The AI unlock has begun"
video_id: "h5zkzon0gM4"
youtube_url: "https://www.youtube.com/watch?v=h5zkzon0gM4"
publish_date: "2026-10-06"
duration: "14:29"
duration_seconds: 869
view_count: 118801
author: "AI Search"
description: |
  How AI is used to mod games. Pass through mod, rebuilding in rust, porting mechanics. Claude Opus 5.5 game mod. Thanks to our sponsor Runway. https://runwayml.com/aisearch-oct 
  Use code MKTG50 for 50% off any paid plan for the 1st month
  
  #ai #aitools #gaming #ainews #singularity 
  
  Resources
  https://github.com/rehan-remade/universal-modder
  https://github.com/morluto/rea
  https://github.com/trevaintdead/ai-game-modding-guides
  https://github.com/bethington/ghidra-mcp 
  https://github.com/HexRaysSA/ida-mcp 
  https://github.com/icsharpcode/ilspy 
  https://github.com/SamboyCoding/Cpp2IL 
  https://github.com/boykopovar/AnyPS5
  https://github.com/yuriolive/PortPS5
  
  0:00 Intro
  0:55 Reverse engineering binaries
  3:34 Pass through mod
  5:40 Reverse engineering
  6:25 Runway
  7:49 Rebuilding in Rust
  9:06 Platform compatibility
  10:00 Porting mechanics
  11:50 Examples and how to prompt
  12:31 Cracking software
  13:08 Inflection point
  
  
  See my X for more AI updates: https://x.com/aisearchio
  
  Newsletter: https://aisearch.substack.com/
  Find AI tools & jobs: https://ai-search.io/
  Support: https://ko-fi.com/aisearch
  
  Here's my equipment, in case you're wondering:
  Lenovo Thinkbook: https://amzn.to/4jWeKwH
  Dell Precision 5690: https://www.dell.com/en-us/dt/ai-technologies/index.htm?utm_source=AISearchTools&utm_medium=youtube&utm_campaign=precisionai#tab0=0 
  GPU: Nvidia RTX 5000 Ada https://nvda.ws/3zfqGqS
  Mic: Shure SM7B https://amzn.to/3DErjt1
  Audio interface: Scarlett Solo https://amzn.to/3qELMeu

yt_tags:
  []


# AI-enriched metadata
content_type: "Tutorial"
primary_topic: "AI Tools"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Product Managers"
entities:
  companies:
    - "OpenAI"
    - "Meta"
    - "Microsoft"
    - "Adobe"
    - "GitHub"
    - "YouTube"
    - "Runway"
  people:
    []
  products:
    - "Claude"
    - "Runway"
    - "Make"
    - "MCP"
    - "Opus"
    - "Projects"
    - "Nano Banana"
  models:
    - "Claude Opus"
concepts:
  - "Ai can read almost any game, reverse engineer the code of it, or make advanced mods to the game"
  - "That all proprietary software could potentially just get cracked and cloned with ai"
summary:
  - "# The AI unlock has begun

Folks, this is pretty crazy"
keywords:
  - "adobe"
  - "ai-agents"
  - "ai-news"
  - "ai-tools"
  - "anthropic"
  - "career"
  - "claude"
  - "coding"
  - "frameworks"
  - "github"
  - "make"
  - "mcp"
  - "meta"
  - "microsoft"
  - "nano-banana"
  - "openai"
  - "opus"
  - "product-management"
  - "projects"
  - "prompting"
  - "runway"
  - "tutorials"
  - "workflows"
  - "youtube"
---

# The AI unlock has begun

Folks, this is pretty crazy. We've now reached a point where AI can seriously disrupt the software and gaming industry. People are now cloning the characters or systems from one game and then just mashing them up with another game. Like, you can put Minecraft mechanics inside GTA. You can take Spider-Man and drop him into a Batman game. You can take Mario and drop him into another game. You can recreate the parkour system from Mirror's Edge and put it inside Skyrim. The crazy thing is everything works. It's pretty seamless and anyone can just do this by prompting an AI. Like you don't even need much technical knowledge. So in this video we're going to go over exactly what's going on, how it works, and how to actually do this yourself. And this has far bigger implications than just video games. So even if you're not into video games, it's still worth watching this video. Let's jump right in. Let's rewind back time to where this all started. So the catalyst for all of this is actually a few weeks ago when OpenAI released GPT6 Astra on their official release page. If you look at its performance on this particular benchmark called S sur bench, the success rate of GPT6 Astra after four attempts is over 99%. Now this benchmark basically measures how good a model is at reverse engineering software from binaries. If you have no idea what this means, let's go over it really quickly. So when a software or video game company makes a product, they first write it using code, right? This is like the original recipe. Well, after they're finished, this source code is then compiled into something called a binary, which is like the finished product. This is the software or video game that consumers see. So you can think of the source code as like the recipe for baking a cake and then the compiling as the baking process and the binary as the finished cake. In fact, for decades, software companies have relied on this gap so that no one can easily copy or modify their software. If no one can see the original recipe, then you can't really copy it, or at least it's going to be really hard to reverse engineer a product just by looking at the binary. Well, here's where the current state of AI changes everything. Because as you can see, GPT6 Astra is able to just look at the binary of any software and reverse engineer it with an over 99% success rate. And the recently released Claude Opus 5.5 appears to be even better. So, for example, AI has already completely decompiled games like Super Smash Brothers, Mario Kart 64, Halo, Kingdom Hearts, and Fire Emblem, just to name a few examples. Let's take a moment to understand how massive this is. This means AI can read almost any game, reverse engineer the code of it, or make advanced mods to the game. And it's not just video games. AI can literally just look at any piece of software, whether it's Photoshop, Microsoft Office, or potentially even an entire operating system, and kind of reverse engineer how it works. It's basically eroding the gap between the binary and the source code. And this means that all proprietary software could potentially just get cracked and cloned with AI. So, uh, you know, now's probably a good time to sell any SAS stocks you might be holding if you haven't already. Now, in this video, I ain't going to show you how to use AI to crack Photoshop because there are, of course, legal implications for this. So, let's talk about some safer use cases for this, like modding or mashing up games. In fact, there are various ways to use AI to mod games. So, let's go over the different approaches. One pretty simple approach is called a pass through mod. This is like putting Minecraft inside GTA. What happens here is that you're not rewriting Minecraft or GTA from scratch. Instead, you keep the original games or systems, but you just get AI to build a layer that connects them together. For example, suppose you use a Minecraft player to place TNT in a certain location. The mod layer from the AI could translate that into something that GTA understands. For example, spawn an explosive object at this position. And then when the TNT explodes, this mod will tell GTA to apply an explosion at that place. So, think of this as like a bridge that translates actions and physics between two games. This still requires that you have both games running on your system first. Or here's another example where you can basically port Spider-Man inside a Batman game. Now, while this looks impressive, it's actually the most limited option because you're still constrained by the original engines of the game since you're kind of connecting both games using a bridge, it's kind of like duct tape. So, it gets the job done, but you sometimes get issues with things like collision and physics. Now, if this is of interest to you, here's how you can run it. The nice thing is there are already a ton of pre-built tools or skills which you can just give any AI agent to do this. So, one of the most popular ones is called Universal Modder. I'll link to it in the description below. And they have this mashup skill which allows you to do a pass through between two games. So, for example, you can just paste the link to this GitHub and then prompt any AI agent like GPT6.1 Soul or GPT6 Astra or I've heard that Claude Opus 5.5 works really well and then just prompt it to do a pass through between two games. Now, instead of this universal modder, here's another really similar tool which works just as well called reverse engineer anything. And again, you can just like link your AI to this GitHub, which already contains like pre-built skills and MCPs, which it can connect to. All right, so that covers pass through mod. Let's move on to another approach, which is building the software that runs the game. This is a lot more ambitious and a classic example of this is like pulling up a vanilla World of Warcraft except the character is on a skateboard. Now, how this works is you just give the AI model the game and it plugs it through a reverse engineering tool like Gedra, which I'll link to in the description below. And the AI basically figures out how everything in the game works, like the animations, the maps, the models, the mechanics, and it attempts to basically rewrite the game, for example, in another language like Rust. Now, you don't have to use Rust, but it turns out that most of the Frontier models today seem to be really good at this language. And that's why you see a lot of game rewrites specifically in Rust. If you create videos, ads, or pretty much any kind of visual content, definitely check out Runway, the sponsor of this video. Think of it as an all-in-one creative AI platform where you can carry out all your creative workflows. You can access the best image generators like GBT image and Nano Banana, as well as the best video generators like Cance and Cling. all through a single platform. But what makes Runway especially interesting is that it goes way beyond just generating individual clips. For example, with Runway Agent, you can simply describe the video you want to make. And it can help develop the concept, create the scenes, generate dialogue and voice over, add music, and turn everything into a complete video through one conversation. And if you already have footage, Olif 2.0 lets you edit it just by describing what you want changed. You can relight a scene, completely restyle it, change the environment, or add and remove objects without having to reshoot anything. You can even build reusable workflows that chain multiple AI tools together. So once you've figured out a process you like, you can automate it and generate consistent content at scale. So whether you're making ads, social content, product videos, films, or entire marketing campaigns, Runway gives you the models, editing tools, and automation you need to go from an idea all the way to something you can actually publish. Check out Runway using the link in the description below or by scanning the QR code and use my code for 50% off the first month on paid plans. Now, for this to work, you still need to own a copy of the game first, but you're basically feeding that through the AI to like rebuild it into another engine. And this allows you to do a lot more customization with the game. So, another cool example of this would be like rebuilding Call of Duty Modern Warfare in a new Rust engine and then combining it with a Minecraft world. So, you can shoot mobs, destroy blocks with guns, and blow them up with grenades, which is pretty crazy. Now, if you're interested, here are some tools that might help. So, in order to do this, you need to give the AI model some reverse engineering tools. And one of the most popular ones is GEDra. There's already a Gedra MCP server, which is a set of skills you can directly link to your AI agent. So, again, you can just copy and paste this GitHub repo into your prompt. Another similar reverse engineering tool is called IDA. There's also an MCP for this which AI agents can use. So I'll also link to this GitHub in the description below. And then specifically for .NET or Unity style games, you can also point the AI to these tools to help decompile the games. For .NET apps, you can use IL Spy and for Unity games, you can use this one. So if you're interested in rewriting a current game that you own, you can just point your agent to these GitHub repos and ask it to rewrite your game in Rust or something like that. And once you've decompiled the game, another cool application is that you can potentially bring the game to another platform, like making a regular PC game playable in virtual reality. For example, you can take a decompiled version of Super Mario Galaxy and with the help of AI, you can create a VR mod for it to run on the Meta Quest. The same thing is happening with other games like Mario Kart. So, here's an example where you basically decompile the game and then you can rebuild it for a virtual reality headset. Another really awesome application is making PS5 games compatible with PC. There are already several projects including any PS5 and also port PS5 that are using AI to do this. So, some cool successful examples are like God of War Sons of Sparta as well as Dead Cells Return to Castlevania. All right, moving on to the next approach. This is even cooler. So, this involves copying a particular mechanic from a game and porting it into another game. This is where we start to see some really cool mashups. For example, you can get AI to copy just the parkour movements from Mirror's Edge and put them into Skyrim. And apparently, this is quite easy for Claude Opus or GPT Astra to do. It was done in around a day. And this parkour action can also potentially be adapted to many other games. Another example would be like copying the trick physics of Skate 3 and dropping it into Call of Duty. Or you can also drop the same physics into World of Warcraft as you can see here. Or here's another crazy example where we're playing in a Minecraft world, but it has Skate 3 and Call of Duty Dynamics. Or here's another ridiculous mashup with Skyrim, Escape from Tarov, and Spider-Man all jumbled together in just one game. So, this opens up a ton of possibilities, especially for game design, because you can now just use AI to essentially extract any physics or mechanics or animation from any game. You can take anything you want and then transfer it to a new game that you're developing without having to necessarily code that particular thing from scratch. Think of it as like copying and pasting various elements from different games to create a completely new game. Now, to do this, fortunately, you don't have to prompt everything from scratch. For example, again, using this mashup mod skill from Universal Moder, it already contains instructions for the AI agent on how you can port content from one game into another game. So, a link to this main GitHub repo, which you can just point your AI agent to. And again, another really useful repo is this reverse engineer anything one, which contains a ton of pre-built tools and skills for your AI agent. And finally, if you need more guidance, I'll also link to this resource which contains step-by-step instructions on like how to actually do the stuff I've shown you in this video. So, this includes a full example of a pass through mod from start to finish, as well as another example of rewriting a game in Rust. And if you're wondering about what exactly to prompt the AI, well, they've included a section here on the prompting and the workflow. The thing to note is that there are no magic prompts. I mean, the current Frontier models, especially Cloud Opus 5.5, are already really good at just understanding your intent. So, you can even just use a really simple prompt like, I want XYZ for this game, or I want to put this character from this game into another game, and then you can just link it to the MCPS that I shared. Now, obviously, this doesn't just stop at video games. In principle, the same techniques can also be applied to reverse engineering proprietary software like Photoshop or Premiere Pro or Microsoft Office. But to be clear, you should absolutely not try to do this. In fact, this channel strictly condemns such actions. Instead, you should do the responsible thing and pay hundreds of dollars every year on a subscription, which is impossible to cancel, and keep paying for software which you don't own, which hardly improves at all. That's the responsible thing to do. Don't you dare try to reverse engineer Adobe Creative Cloud and run it for free. So, going back to our original diagram here at the start of the video, AI has now reached a pretty crazy inflection point. This stat shows that it can successfully reverse engineer almost any game or software with an over 99% success rate. So, this is going to have huge implications for like software and video games. And you know, because AI is so good at like reverse engineering binaries now, it's probably very likely that they're actually reverse engineering all the games and software in the world and using that base code as training data for their future AI models. I mean, the current generations of AI models are already pretty good at vibe coding games or software, but we can expect the next generations of AI models to become even better at vibe coding this stuff completely from scratch. How will this affect the future of gaming and software and what are the legal implications of this? Let me know in the comments below what you think. As always, I will be on the lookout for the top AI news and tools to share with you. So, if you enjoyed this video, remember to like, share, subscribe, and stay tuned for more content. Also, there's just so much happening in the world of AI every week. I can't possibly cover everything on my YouTube channel. So, to really stay up tod date with all that's going on in AI, be sure to subscribe to my free weekly newsletter. The link to that will be in the description below. Thanks for watching and I'll see you in the next one.

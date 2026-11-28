---
title: "Google cracks recursive self improvement"
video_id: "YOsQULgqgNA"
youtube_url: "https://www.youtube.com/watch?v=YOsQULgqgNA"
publish_date: "2026-11-27"
duration: "14:20"
duration_seconds: 860
view_count: 168187
author: "AI Search"
description: |
  Google’s new breakthrough on continual recursive self improvement. Thanks to our sponsor Higgsfield. Try it today https://higgsfield.ai/s/EFXMKG 
  
  #ai #aitools #agi #singularity #llm
  
  00:00 Continual RSI
  00:51 What’s a harness
  02:08 RSI of the harness
  03:48 Self improvement memory
  04:50 Ablation experiment
  06:09 Higgsfield GPU harness
  07:29 SIM vs no SIM
  10:30 Why this matters
  11:42 Unified harness
  13:03 Harness vs AI model
  
  
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
content_type: "Framework"
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Executives"
  - "Product Managers"
entities:
  companies:
    - "Google"
    - "Nvidia"
    - "DeepMind"
    - "X"
    - "YouTube"
  people:
    []
  products:
    - "Claude"
    - "Claude Code"
    - "Gemini"
    - "Make"
    - "Opus"
  models:
    - "Claude Opus"
    - "Gemini"
    - "Gemini 3"
    - "DeepSeek"
concepts:
  []
summary:
  - "# Google cracks recursive self improvement

No waifuss in this video, but Google DeepMind dropped a very interesting paper recently involving what they call continual recursive self-improvement"
keywords:
  - "ai-tools"
  - "anthropic"
  - "claude"
  - "claude-code"
  - "coding"
  - "deepmind"
  - "frameworks"
  - "gemini"
  - "google"
  - "make"
  - "nvidia"
  - "opus"
  - "product-management"
  - "tutorials"
  - "workflows"
  - "x"
  - "youtube"
---

# Google cracks recursive self improvement

No waifuss in this video, but Google DeepMind dropped a very interesting paper recently involving what they call continual recursive self-improvement. The core idea here is how we can give AI a persistent memory of its own past mistakes, allowing it to continuously improve itself rather than starting from scratch every single time it starts a new task. So, that's what we're going to go over in this video. This is quite technical, but as always, I'm going to break this down into simple terms so it's easy to understand for everyone. Let's jump right in. First of all, the title here is a bit misleading as this isn't about getting an AI model to improve itself recursively in the strictest sense, but it's about recursively improving the harness around the model, which in turn still lets the AI kind of learn or get better over time. Now to understand what this paper is about, we first need to understand what exactly a harness is. You see, when you interact with a large language model, especially one of the frontier ones, it usually doesn't do all the work by itself. Instead, there's also a harness that kind of controls or guides what it does. Now, there are some well-known harnesses designed for the Frontier models. For example, Claude Code is the harness for Claude. Codeex is the harness for GPT. Anti-gravity is the harness for Gemini. And we also have DeepSeek harness for DeepSeek just to name a few examples. You can think of the harness as like the software wrapper around the model. It supplies the workspace, tools, memory, and rules for the AI. It allows the AI to search the web, read or write files, or call other tools. The harness also manages memory and context so that the model doesn't lose track of the session, especially if it's really long or involves multiple steps. It also sets permissions and asks for human approval before letting the AI do risky stuff. So, you can kind of think of the AI model as the engine. It's able to generate raw power and speed, but it can't really steer or break or go anywhere on its own. And the harness is basically the chassis, the steering wheel, and the brakes. So, the harness is incredibly important, and some would argue it's as important as the AI model itself. And recently, there's been a lot of research about optimizing the harness. As you can see from all these citations, in fact, that's what the recursive self-improvement in this paper is referring to. They basically figured out how to get the AI model to use feedback from its own sessions to rewrite and optimize its own harness. And this in turn allows the AI to perform better within the harness. So, it's like a positive feedback loop. Now, this sounds great in theory. The AI's performance would get better and better as the harness becomes more optimized. But what happens if we want to switch the underlying model? Let's say we spent a few weeks using Claude Opus 5.5 to optimize and evolve a harness around it. But now we want to move that harness over to a Gemini model. Ideally, we'd want all this optimization to transfer over to the new model because that would save us time from starting a new harness from scratch. And surely the new AI model should be smart enough to adapt to the harness, right? Well, unfortunately here the researchers actually showed the opposite. So they took a harness that had been recursively evolved and optimized by a claude opus model and they tested it on some tasks involving a simulated desktop environment. So things like using an operating system, opening browsers, and working with different files. But then they used that harness with a Gemini model and it actually performed worse on these tasks. Sometimes even worse than if they just used a completely blank harness from scratch. So here they showed that a highly optimized harness actually hurts the performance if you switch the model. So it seems like everything learned from the self-evolution from the Opus model wasn't actually passed on to the new Gemini model using the same harness, which is not ideal. So instead, here's the core innovation of this paper. They call this SIM, which stands for self-improvement memory. Rather than just passing down the final code of the evolved harness, SIM passes down a structured persistent record of the entire improvement process. So, it's basically giving the AI a notebook of its own evolutionary history. And here's how it works. Each SIM record basically contains several structured fields. First, it logs the root cause of the problem that it encountered, like the actual bug. Then, it logs the rationale and also the predicted outcome of that fix. And finally, the observed outcome. Plus, it also logs the specific model and domain where the errors occurred. Basically, it records what it tried and what actually worked or failed. Now, you might be thinking, "That seems like way too much information. Wouldn't it be enough if we just told the AI what the bug was? Why does it need this whole history plus predicted versus observed outcomes or which specific model it was using? It seems like overkill." Well, the researchers thought the same thing. So to test if all this data was actually necessary, they ran an ablation experiment. An ablation is where you basically remove a factor to see if that affects the results in any way. So they tested a condition called problem only memory, meaning they stripped out the history, the outcomes, and just gave the AI the list of bugs. And the results were pretty clear. The full SIM record consistently beat just the problem memory across the board. In fact, in some cases, having problem only memory actually performed worse than having no memory at all, which is kind of strange, but you can kind of think of it like this. Knowing what the problem is doesn't give the AI the historical evidence of what was actually tried and how it failed. So, here's a theoretical example where the AI has to learn how to fix a pipe leakage. If you just tell the AI the pipe leaks, it might try the exact same brand of sealant that failed before. It just gets stuck in a loop of repeating past mistakes. But if the sim records everything like we predicted, this sealant would work, but the outcome was that it didn't work. Well, now the AI has actionable intelligence. It has the whole picture to decide what to do next. In fact, the paper highlights a nice example involving a series of tests called Terminal Bench. Here, the AI is basically put in a simulated environment where it needs to execute code in a command line terminal. If you want to run the latest AI models or make 3D animations without spending thousands of dollars on a GPU, definitely check out Higsfield, the sponsor of this video. They just launched Higsfield GPU harness, which is like a cloud computer that you can access directly from your browser. You can rent some of the most powerful Nvidia GPUs, including the H200 and even the B300 with a whopping 288 GB of VRAM. But what's especially impressive is that you can connect this directly to Claude or Chat GPT and get AI agents to operate the software for you. For example, you can get Claude to create some complex 3D animations in Blender. The AI agent can autonomously build the 3D scene, set up the lighting, animate the objects, and render the final video using the cloud GPU. Plus, you can open up the actual Blender interface, and manually edit everything yourself. It also supports other popular software like Unreal Engine, Houdini, and Da Vinci Resolve. Or you can run open-source AI models and even import your own custom Loras from HuggingFace. And the best part is that your build by the second, so you only pay for the time your cloud computer is running. Higsfield GPU gives you access to incredibly powerful hardware without having to invest in an expensive workstation yourself. Try it today using the link in the description below. Now, first they gave it an older series called Terminal Bench 2.1. And initially, the AI model kept running into a recurring bug. It would claim the task was complete without verifying if the code actually ran. In other words, it was hallucinating success. But after they applied this new recursive self-improvement technique, it actually learned to build something called an interlock gate into its harness. This is a strict piece of middleware that basically blocked the AI from triggering the task complete function unless there was proof of execution without any errors or crashes. So it kind of built a safety switch in the harness. Now this whole process, the bug, the rationale, and this new middleware was recorded in a SIM record. And here's where it gets fascinating. They then tested the AI in an even harder data set called Terminal Bench 4. Here the tasks are way more complex. For example, the AI has to write code to route photonic waveguides on a circuit board. And this requires the AI to find an optimal solution. So, it's not just about making sure the code runs without crashing, but it also needs to find the absolute shortest and most efficient path. Now, for this test, the researchers looked at what happens with and without SIM. If they run it without SIM, the AI kind of panics. It doesn't understand why it's failing because the middleware is telling it the code is fine. It looks at this interlock gate that was created in the previous step, but it doesn't know why this was built and it assumes the gate itself is broken. It then starts like editing and tightening the gate, causing a ton of deadlocks and errors. And then it mistakenly blames its own edits. It messes up this old safety protocol and gets completely stuck in a loop of failing the benchmark. Now, let's see what happens if they run it with SIM. The AI encounters the exact same failure at first, but this time before it touches the harness code, it queries its SIM memory. In other words, it reads its notebook and parses the rationale of the previous stuff. It understood that this interlock gate was put here in a previous step strictly to ensure verification. It understands not to break this. So, it keeps this gate intact. Instead of panicking and deleting code, it calmly opens a new SIM entry. It diagnoses the problem and it writes a brand new piece of middleware that basically audits for solution quality and it adds this to the harness alongside the gate from the previous step. So it could kind of scale in complexity without collapsing under its own weight. And as you can see from these performance scores, the instance with sim performed much better on terminal bench 4 compared to without the sim. Now this is just one example. Instead of terminal coding, they also tested it on a ton of different domains like text classification, agentic work, and engineering design, which required completely different types of reasoning. And the results were remarkably consistent. Having full SIM records scored much better than just passing on the edited harness without any records. Even if they used different data sets or different models, the instance with SIM performed much better. Now, if you're watching this and wondering why does this matter, it comes down to the sheer speed of model iteration. We're getting new models faster and faster. For example, it took 29 months to get from GPT4 to GPT5, but it took less than half the time to get to GPT6. Heck, Google just dropped like four new models in the span of a month. It's accelerating like crazy. But here's the problem. If the AI companies have to reoptimize their harness, including like the logic for error handling and execution loops, from scratch every time a new model is released, then progress becomes severely bottlenecked. This would take way too much time and effort. But with this new SIM method, it allows for what the researchers call continual recursive self-improvement. It means the infrastructure surrounding the AI can continually evolve, accumulate wisdom and adapt to new models without forgetting the hard-earned lessons from the past. It effectively decouples the intelligence of the harness from the specific version of the model. And this leads to a very fascinating implication. You see, up to now, we've been talking about using SIM to upgrade the harness sequentially. We talked about how we could switch the underlying model without affecting performance. But here's the wild part. The researchers also showed that you can use sim to design a single shared harness that works across different models simultaneously. They took Grock 4.2, Claude Opus 5.5, and Gemini 3.8 Flash. These are like models with completely different architectures trained on different data from three different companies. It's really hard to make a single unified harness that works for all three of these models without things breaking down. But because this new sim design isn't specialized for any specific model, instead it's just logging the logic of its learnings and failures, by pulling the feedback from all three models into one sim memory bank, they basically allowed the models to collaboratively write the harness together. So Grock might encounter an error and then it logs the root cause and the fix. And then later, Gemini runs into a similar task, queries the sim memory and reads Grock's record and applies this logic to its own execution. It's basically one unified middleware which all three models can work together to improve simultaneously. And the crazy part is that this harness performs on par or even better than harnesses that were specialized for each model separately. This proves that the data stored in sim can actually be generalized. It's essentially like shared cognitive infrastructure. Now, this raises a pretty interesting question. If an AI's harness can persistently self- evvolve if it can remember its past and seamlessly adapt across totally different models, is there a potential future where the harness actually becomes more valuable than the AI model itself? Like maybe the LLM become interchangeable commodities while the evolving harness with its deep historical memory actually becomes the key to an AI's performance. Anyway, that sums up my explainer on this new Google paper about continual recursive self-improvement. Again, the title is kind of misleading because it's not like the AI models themselves being able to recursively self-improve, but they do show how you can get one or multiple AI models to continuously improve the harness around it through its learned experience, which in turn allows the underlying AI model to also improve its performance over time. So, a pretty interesting paper. Let me know in the comments what you think of this. As always, I'll be on the lookout for the best and latest AI tools to share with you. So, if you enjoyed this video, make sure to like, comment, subscribe, and stay tuned for more content. There's so much going on, I might not be able to cover everything on my YouTube channel. So, also be sure to follow me on X and subscribe to my free weekly newsletter for even more updates. I'll link to these in the description below. Thanks for watching and I'll see you in the next one.

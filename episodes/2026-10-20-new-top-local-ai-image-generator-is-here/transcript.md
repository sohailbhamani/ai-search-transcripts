---
title: "New top local AI image generator is here!"
video_id: "cUeZMUGCxrw"
youtube_url: "https://www.youtube.com/watch?v=cUeZMUGCxrw"
publish_date: "2026-10-20"
duration: "21:56"
duration_seconds: 1316
view_count: 110071
author: "AI Search"
description: |
  MOSS Image review & tutorial. How to use MOSS Image in ComfyUI. How to edit images with MOSS. Thanks to our sponsor Higgsfield. Try it today https://higgsfield.ai/s/theaisearch-rxYPHC
  
  #ai #aiart #imagegenerator #aitools #ainews #agi
  
  https://huggingface.co/Comfy-Org/MOSS-Image
  https://huggingface.co/lodestones/MOSS-Image-SFT-8-steps-dmd/blob/main/lora.safetensors
  https://huggingface.co/lodestones/Kromoss
  https://github.com/ostris/ai-toolkit
  
  Also see
  ComfyUI tutorial: https://youtu.be/g74Cq9Ip2ik
  Krea2 tutorial: https://x.com/aisearchio/status/2075660074308313598
  Ideogram4 tutorial: https://youtu.be/OA4gchz1Zcs
  
  00:00 MOSS Image intro
  00:37 Specs and demos
  02:14 MOSS Image vs Krea 2
  03:01 How to use MOSS in ComfyUI
  08:33 How to use layout control
  11:03 Higgsfield
  12:30 How to add loras
  15:20 Better checkpoints
  16:05 How to make it faster
  17:50 How to edit images
  20:28 How to train loras
  
  
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
primary_topic: "AI Strategy"
difficulty: "Intermediate"
audience:
  - "Engineers"
  - "Product Managers"
entities:
  companies:
    - "Box"
    - "YouTube"
  people:
    []
  products:
    - "Claude"
    - "Make"
    - "Nano Banana"
    - "Canvas"
  models:
    - "CLIP"
    - "SDXL"
    - "Flux"
concepts:
  []
summary:
  - "Folks, we have a new open-source image
generator, and this is by far the best image model in its weight class"
keywords:
  - "ai-news"
  - "box"
  - "canvas"
  - "claude"
  - "frameworks"
  - "make"
  - "nano-banana"
  - "tutorials"
  - "workflows"
  - "youtube"
---

# New top local AI image generator is here!

Folks, we have a new open-source image
generator, and this is by far the best image model in its weight class. This
has a ton of knowledge. It can generate a ton of different things, including
really complex infographics and diagrams with text. Plus, you can also generate
certain crops with this. And the best thing is this is really tiny. You can
even run this with 4 GB of VRAM or less. So, it's called Moss Image. And in this
video, we're going to go over some demos. And of course, I'm going to show
you how to install it, plus how to customize it even further. How to make
this faster, how to make it even better quality, how to even use this for image
editing, and more. So, let's jump right in. First of all, let's go over the
specs of this. So, this is a really small 5 billion parameter image
generator. So, the quantized versions of this are small enough to fit on even
low-end consumer GPUs. Now, keep in mind that this is just a text to image
generator. So, you can't edit images semantically using natural language like
Quinn image 2.1 or nano banana. But later in the video, I'm going to show
you some hacks to still get moss to edit images. And the nice thing is this also
supports layout control. So, you can draw boxes over your canvas to control
the exact composition of where things are in the image. So, first of all, here
are some examples for your reference. Note that this can generate very
realistic images. It's also great at generating anime. It's also really good
at different artistic styles. You can also get it to generate some super wide
or tall images, so it doesn't have to follow conventional aspect ratios. Now,
this moss image has incredible knowledge packed in. So, here are some examples of
different celebrities that it knows right out of the box. You don't even
need to add Lauras or reference images for this. Or here are some examples of
anime characters that it knows. And then here are some other examples of video
game characters. And then finally, here are also some of my tests on various
brand names and car models. So, it's really impressive how they jam-packed
all this knowledge into just 5 billion parameters. And it's absolutely
incredible at generating text. So, the following examples are completely
generated with MOSS. So, you can easily get it to generate like text diagrams or
infographics or other images with a ton of different elements. Now, if we
compare this to the current leading open textto image generator, Creata 2, then
at least from my initial tests, Crea 2 does perform better, but this is
expected because Crea 2 is like more than twice the size of Moss image. So,
of course, it'll be slightly better quality. But if you can't fit Creata 2
on your GPU or if you want to run images even faster, then Moss image is by far
the best model in its weight class. It just seems to have much better
understanding and a lot more flexibility than the closest competitor which is Z
image which is still bigger at 6 billion parameters. But at 5 billion parameters,
you can see that MOSS image is incredibly capable. So if this is of
interest to you, next we are going to go over how to install this and run it for
free and unlimited times offline on your computer. Now, there are many ways you
can use Moss image locally on your computer, but one of the easiest and
most customizable ways to use it is with a platform called Comfy UI. If you
haven't heard of this, this is like one of the most popular and free platforms
for running open-source image, video, and audio generators on your computer.
In fact, if you're not familiar with it, see this video first where I go over how
to install and use Comfy UI. Now, assuming you do have Comfy UI installed,
the first step is to update it to the latest version. Now, for me, I'm using
the Windows portable version, which is the recommended version. And I'm simply
going to click into this update folder, and then click on update comi.bat. And
this is going to open up a terminal to update my Comfy UI to the latest
version. So, let's give it a few minutes to run this. All right. Afterwards,
let's press any key to continue to automatically exit the terminal. And
next, we can proceed to open up Comfy UI. So, let me start that up.
Afterwards, simply click on templates in the left sidebar. And then at the top
here, type in MOSS and you should see these MOSS image workflows. Now, note
that there are actually two different versions of MOSS image. There's a MOSS
image SFT, which is specialized for image generation, and then there's also
a MOSS image base, which is more for training and fine-tuning it further. So,
if you're just generating images, I would highly recommend you just go with
this MOSS image workflow. So, let me show you that really quickly. I'm also
going to go over this layoutg guided workflow afterwards which allows you to
control the composition of your image with bounding boxes. But for now, let's
just click on this textto image workflow. And you should see this. Now,
at the start, you might see some missing models. So, you can simply click on
download over here for it to automatically download the model. But
what I like to do instead is actually go to the folder and manually select the
right model to download. So, let me show you that really quickly. I'm going to
link to this page in the description below. First, we need to click into
diffusion models. And again, note that here there are two types of MOSS image
models. There's the base model, which is mostly used for training and
fine-tuning. So, if you're just using it for image generation, I would highly
recommend the SFT models instead. There are two different versions of this.
There's a full BF-16 version, which is 10 GB. So, this would be higher quality,
but it's also like almost two times larger than the other one, which is a
more compressed int8 conro version. This has slightly lower quality, but this can
fit with lower VRAM. So, it depends how much VRAM you have. If you have over 8
gigabytes, then you could try this full BF-16 version for better quality.
Anyway, for me, I'm going to download this INT8 Conrad version. So, let me
click download. And this goes in Comfy UI in models and then into Fusion
models. Let's click save. All right. Afterwards, we also need to download the
text encoder. So, let me click on that. And then here we are given three
different versions. There's a full BF-16 one followed by a medium-sized INT8 one
and then an even smaller W488 one. Now, of course, the biggest one gives you the
best quality, but you'll need more VRAM to fit this. For me, I'm just going to
go with the smallest one. This is still pretty good quality. So, I'm going to
click on download. And this goes in Comfy UI in models and then in text
encoders. Let's click save. And then finally, we also need to download the
VAE for this. So, let me click into this folder. And again, we have two different
versions. There's a full version and then a smaller version which is 250
megbytes. I'm just going to download the smaller one. So this goes in comi in
models and then in VAE. Let's click save. All right. After downloading
everything, simply press R to refresh your model list. And then down here,
let's click on the dropown and select the appropriate model. So for the first
dropown, let me select the MOSS image model that I downloaded. And then for
the clip, I'm going to select this Quen 3.59B.
And then for the VAE, I'm going to select flux to small. And that's pretty
much it. So, let's walk through this really quickly. Here is where we set the
aspect ratio. And then here's the megapixels. So, a square image at 1
megapixel is roughly 1024x1024. And then over here is where we would
enter your prompt describing the image. And if we set this toggle to true, it's
basically going to enhance your prompt further. And in theory, this should help
you generate a better looking image. And then over here is where we would enter a
negative prompt describing all the things you want to exclude from your
image. And then down here are the standard sampler settings. So the first
one is the seed. This is basically the unique ID of your image. If you set all
the settings the same plus you use the same prompt and the same seed, you're
going to get the exact same image as before. If you want to keep the exact
same prompt but generate a different looking image, then you can just change
the seed to another number to generate a slightly different image. And then the
number of steps is basically how many well steps it takes to generate the
image. In general, the more steps you use, the higher quality it'll get, but
it tends to not make much difference after like 40 to 50 steps. And of
course, the more steps you use, the longer it'll take to generate the image.
And then the CFG is basically how literally you want the AI to follow your
prompt. So if you find that your image is not following your prompt exactly,
you can try bumping up the CFG to a higher value. And then for the sampler
anduler, this is basically the algorithm used to generate the image. There are a
ton of different sampler anduler types. So feel free to play around with these.
I'm just going to go with the defaults. And that's about it. So let me press run
and let's see how long this takes on my GPU. Note that I'm using an RTX 5000 ADA
which only has 16 GB of VRAM. All right, that was pretty quick. It only took
around 25 seconds to generate this. And here's our result. So pretty simple.
That's text to image. Next, let me pull up templates again. And again, at the
top, I'm going to type in moss. And next, I'm going to show you how to
control your composition using bounding boxes. Again, there are two different
workflows you can choose from. One is using the base model, which is mostly
used for fine-tuning. So, if you just want to generate images, then I would go
with this one. So, let me click on this. Here's what the workflow looks like. If
you followed my instructions for the previous workflow, then you should
already have all the models downloaded over here. Now one thing to note is that
some of you might see this message bounding boxes node 2.0 only. So if you
see this what you need to do is to click on settings in the lower left corner and
then at the top here toggle this to enable nodes 2.0. So let me toggle this
and then afterwards you should see this bounding box layout like this. All
right. Next let's go over the settings. So let's start with this one again.
Here's where we would select the resolution in megapixels. And then over
here is where we can control the composition of your image using bounding
boxes. So after you draw a box, you can also move elements around or click on it
and press delete to delete the element. In fact, let me press on clear all so we
can start from scratch. Let me draw something over here and then write a
beautiful woman wearing a bikini sitting on a sofa. So let's have a red sofa over
here. I'm going to write red sofa and then let me draw another element over
here. Let's write coffee table with house plants. Let me drag another
element over here and write her right foot lifted up. And then let me drag
another element over here. And let's write a window with a T-Rex outside. Let
me also drag another one here. And let me put it here. And then write her hand
holding a can of Coke. And then let's also add a Nudo poster on the wall.
Let's write an Aruda poster on the wall. And then over here is where we would add
a description of the entire image. So I'm going to write something like this.
And that's pretty much it. And then here we have the same settings as before,
such as the seed, number of steps, CFG, etc. So let me press run and let's see
what we get. All right. And here's what we get. Indeed, we have a woman wearing
a bikini. She is holding a can of Coke. By the way, the Coke logo is actually
correct, but it's just in Chinese. Her right foot is over here. Plus, we have a
red sofa, a coffee table with house plants, Naruto poster in the background,
plus a T-Rex outside the window. Everything is exactly as I prompted. So,
that's how you can use Moss image with this layout control. If you're doing any
type of content creation, definitely check out Higsfield, the sponsor of this
video. They just launched Higsfield Katana, which is a new AI video editing
tool that works directly inside Claude, allowing you to recreate almost any
viral video with your own characters, products, or footage. And the best part
is you don't need any video editing skills. For example, let's say you find
a really cool clip on Tik Tok or Instagram and you want to recreate it
with yourself as the main character. Simply upload the reference video along
with a few photos of yourself and tell Claude to recreate it using Katana. It
automatically recreates the original video shot by shot, including the camera
movements, transitions, colors, text, and even the audio, but you can swap the
character, objects, or background, or edit whatever you want. What's really
impressive is how it works behind the scenes. Claude analyzes the reference
video and figures out how to recreate every shot. Higsfield then generates any
missing footage and automatically puts everything together into a finished
video. You can also choose from a library of ready-made presets, including
cinematic action scenes, anime style edits, travel montages, and more. And if
you want to experiment, you can create multiple versions of the same video
using different people, products, or images. So, if you want to create
content at scale, Higsfield Katana makes the entire process incredibly easy. Just
connect Higsfield to Claude, type /katana, and start creating. Check it
out using the link in the description below. Now, Moss image is already really
flexible. It has an incredible understanding of different art styles
and characters, but you can also add Loras on top of this for even more
flexibility. If you're not familiar with the term Laura, it's basically a smaller
fine-tune that you add on top of your workflow to, for example, add a certain
character or effect or art style to your image. For example, there's a Laura for
Chainsaw Man. There's another Laura for this ReZero anime style. There's a Lura
for Pale Skin and Redheads. another one for realistic skin. And then here are
some different anime styles. For me, I'm going to try this ink style Laura. So,
let me first click on download. And this goes in Comfy UI in models and then in
Lauras. Let's click save. Now, you can add Loras to both the regular textto
image workflow as well as this layout control workflow. So, I'm going to show
you how to do it for both. Let me just show you the regular textto image
workflow first. So over here, simply click on enter subgraph. And you should
see this. Basically, you just need to place the Laura load before this model
input for the K sampler. So I'm going to click anywhere on the interface and then
type in Laura. And I'm just going to choose this first load Laura node. And
let me place it here. And then I'm just going to drag this over here. And then
connect the output back to the K sampler. And then here I can click on
the dropown and select this ink Laura which I just downloaded. And then here I
can select the strength or basically how much influence I want the Laura to have
on the image. Let's set it to 100%. Now to go back to the workflow, simply press
the escape key. And that's pretty much it. One last thing is that for most
Loras, it actually requires some trigger words. In this case, for the ink laura,
I need to enter these trigger words into my prompt in order to actually well
trigger the Laura. So back here in my prompt, let me paste in the trigger
words over here. Let me also get rid of any related photography keywords down
here and then let's press run. All right, here's what we got. Now, we can
also do the same thing for this layout control workflow. So again, for this
node, simply click on enter subgraph and then again we just need to add a load
Laura node before this model input in the K sampler. So, I'm going to double
click anywhere and then type in Laura. And then I'm going to select load Laura.
And let me just place it here and then connect the model to here. And then
connect this back to the K sampler. And again, I'm going to select this Sumi ink
one. And then back here, instead of realistic photo, I'm going to paste in
these trigger words. And then press run. And here is what we get. So you can see
how it applied this ink splatter art style from the Laura onto my photo. Now,
not only can you add Loras, but if you want even better image quality and
consistency, keep in mind that these original Moss image models are the worst
it's going to get. In fact, people are already fine-tuning full moss
checkpoints. For example, we have this new one called Chromos, and as you can
see from some of these examples, it just looks a lot better and more consistent
than the base moss image model. So, to use this, you just need to download the
checkpoint for this. So, for example, let me click into files and versions and
then diffusion models. And again, we can choose between the full BF-16 one or
this smaller int8 version. So, I'm going to download this one. And like the full
moss model, this also goes in models and then in diffusion models. Let's click
save. And then outwards back in your Comfy UI workflow for the unit model.
Simply select this new chromos model. It's as simple as that. So, those were
some ways to use some custom models to improve the quality of your generations.
Now, for me, Moss image already runs really quickly. It only takes me like 30
seconds to generate an image, but let me show you how to speed this up even more
by like 3 to four times. So, what we actually need to do is download this
eight-step DMD Lura. I'm going to link to it in the description below. Simply
click on download over here. And let's name this something nicer like moss DMD
8 step. So this goes in Comfy UI in models and then in Laura's. Let's click
save. Now again we can apply this to either the regular text to image
workflow or the layout control workflow. Let me just show you how to use it for
text to image. So all the settings are the same as before, but what we need to
do is click on this to expand the workflow. And you should see this again.
And like before we just need to add a Laura before this K sampler. So let me
double click anywhere and then type in Laura. And I'm going to select load
Laura and then place it here. I'm going to take this noodle and connect it over
here. And then connect the output back to the K sampler. And this time I'm
going to click on the drop down and select this MOSS 8step Laura. And at
least for this one, it's recommended to set this at a strength of one. So let's
press escape to go back to our workflow. And the last thing we need to do is
instead of 25 steps, we just need to set this to eight steps. And then for the
CFG, we need to set this to one. Also note that if we set the CFG to one, this
negative prompt won't actually have any effect. So that's kind of the tradeoff.
If you do want your negative prompt to have some effect, then you can like bump
this up by a few decimal points. And that's pretty much it. Again, let's
press run. And now this should run like three to four times faster. All right.
And here's my result. So that's how you can use a Turbo Lura to speed this up
even more. Now Moss is just a text to image generator. So you can't edit
images semantically using natural language like Quinn image 2.1 or nano
banana. But you can still input images for it to edit using plain traditional
image in painting. So let me show you how to do that really quickly. So let's
say I input this image and I want to replace this notebook with a sleeping
cat. Here's how to do so. I'm just on the default text to image workflow down
here. Let's click on enter subgraph. And what we need to do is basically edit and
customize some stuff down here to be plugged into the K sampler. Now, of
course, the first thing we need to do is to upload our image into the workflow.
So, let me double click anywhere on the canvas and then type in load image and
then select this one. And let me click on this to upload my image. Now, I can
hover over this image and then click on this icon to draw a mask over the image.
Here I can edit like the thickness, opacity, hardness, etc. So let me play
around with these settings and then let me draw a mask over this notebook which
I will replace with a sleeping cat. So after I draw the mask, let's click on
save up here. And then the next step is we need to convert this image into
latent space. So let me double click anywhere on the canvas and then type VAE
at the top and we need to select this one VAE encode for inpainting. So let me
click on this and then just place it anywhere here. I'm going to connect this
image to over here. And then for the VAE, I'm going to draw a noodle from
this node and connect it over here. And then for the mask, I'm going to connect
the mask from the image over here. And then afterwards, I just need to link
this latent output all the way to the K sampler over here. Note that once I drop
this, it's going to disconnect the noodle of this one. In fact, I can just
press Ctrl +B to disable or bypass this. So note that this is connected to the
width and height which we set over here. But since now this is disconnected and
disabled, it's not actually going to use that width and height anymore. Instead,
it's going to use the width and height of my input image. And that's pretty
much it. So let's press escape. And then back here, I just need to enter what I
want to generate in the mask that I drew. So let's just write something like
a sleeping cat. And then for this, I'm just going to turn off the prompt
upscaler to make this a bit faster. And then press run. All right. And here's
what we got. Indeed, it was able to add a sleeping cat into my image. So that's
how you can edit images with moss image. It's not great. It's not as flexible as
like Quen image 2.1 or Nano Banana. This is just traditional impainting, but
that's currently how you can edit images with moss. Finally, if you're wondering
how to fine-tune your own Loras for Moss image, one of the best tools to use is
this Ostrus AI toolkit. So, I'll link to this in the description below as well.
They've already added support for training Loras with Moss image. Now,
this is a bit too technical for this video, but at the bottom here, it
contains all the instructions on how to run this. And this even works with Mac
OS. So, that sums up my review and tutorial of Moss image. This is
definitely the best image generator in its weight class. There's so much
knowledge jam-packed into it. It's super flexible. It can generate a ton of
stuff. And this is the worst it's going to get. I'm sure in the next few days,
we're going to get some even better looking checkpoints or fine-tunes for
MOSS. It's kind of like the SDXL era all over again, if you know what I'm talking
about. Let me know in the comments what you think of this, and if you run into
any errors during the installation, welcome to paste the exact error message
in the comments below, and I'll try to help you troubleshoot as much as
possible. As always, I will be on the lookout for the top AI news and tools to
share with you. So, if you enjoyed this video, remember to like, share,
subscribe, and stay tuned for more content. Also, there's just so much
happening in the world of AI every week. I can't possibly cover everything on my
YouTube channel. So, to really stay uptodate with all that's going on in AI,
be sure to subscribe to my free weekly newsletter. The link to that will be in
the description below. Thanks for watching and I'll see you in the next
one.

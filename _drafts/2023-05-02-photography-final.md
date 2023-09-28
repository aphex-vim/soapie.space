---
layout: post
title: using pixel sorting to animate photos
date: 2023-05-02
tags: photography programming art
---
## background
This was my final project for my photography class for the Spring 2023 semester. This post is an adaptation of a presentation that I gave on the work I did for the project. I hope in this format that I can cover things in more depth that I brushed over in the presentation.

## what is pixel sorting?
!["An image of mountains with a pixel sorting effect applied. The effect is glitchy and produces several gradients along each row of the image."](/assets/pixelsorting0.jpg)

Pixel sorting is the application of computer sorting to the data present in images to produce the above effect. This particular image was created by Kim Asendorf, who is one of the earliest pioneers of this technique. His original 2010 code can be viewed [here](https://github.com/kimasendorf/ASDFPixelSort).

## applying sorting to images
The first step to sorting pixel data in an image is deciding how to sort it. This is done by choosing a sorting function. The responsibility of the sorting function is to take each pixel's data, and map it to a singular value. While most commonly a pixel is split into  <span style="color:red">red</span>, <span style="color:green">green</span>, and <span style="color:blue">blue</span> channel, this sometimes makes use of other representations such as [HSL or HSV](https://en.wikipedia.org/wiki/HSL_and_HSV). These are the most common ways that each pixel is mapped to a singular value:

- Sorting by the **hue**, **saturation**, or **lightness** of a pixel's HSL representation.
- Sorting by the **intensity**, the sum of the red/green/blue components of the RGB representation.
- Sorting by the **maximum** or **minimum** value of the red/green/blue components.

Depending on the composition of the original image, selecting a sorting function can drastically change the output of the pixel sorter.

## selectively sorting pixels
!["A blurred mess of white, gray, brown, and black."](/assets/pixelsorting1.jpg)

Although you can't really tell, this is a pixel-sorted picture of my friends dog, Frog. This is an example of what happens if you apply a pixel sorting filter to the entirety of an image. To prevent an image from becoming a blurred mess, pixel sorting software makes use of a **mask** to split the image up into distinct **intervals** that will then be sorted.

!["A black and white image of a beagle sitting on a bed."](/assets/pixelsorting2.jpg)

This is an example of a mask, it was created manually using a threshold filter. Essentially, pixel over a certain brightness has been set to white, and every pixel below a certain brightness has been set to black. The pixel sorter uses this image to determine what parts of the original source image are to be sorted.

!["An image of a black beagle, with a vertical pixel sorting effect applied"](/assets/pixelsorting3.jpg)

The sorter looks at each column of the image and sorts each **interval** of white pixels. In this context, the intervals are each contiguous group of white pixels along the columns of the image. *Note: Intervals can also be the rows of the image, diagonal lines, or even concentric arcs within the image.*

!["An animation with two frames. One shows a pixel art picture of a blue fish with a white background. The second frame is that same fish, but the white background has each contiguous horizontal white line of pixels marked in a different color."](/assets/pixelsorting5.gif)

For instance, if we were to label the horizontal intervals for all the white pixels on the above image with a different color, it would look like this.

## creating animations using pixel sorting
!["An animation of some seaweed paper. The animation shows the intervals of the pixel sort getting larger and smaller, looping infintely."](/assets/pixelsorting4.gif)

To animate the pixel sorting effect, I used some bash scripting to generate multiple frames from the original image, where each frame was generated with slightly different parameters.

Consider this bash script snippet that I used for this animation:
```bash
for upper in $(seq 1 -.1 0.3);
do
	pixel-sorter "seaweed.jpg" -a 90 -u $upper
done
```
This code uses a for loop to run the pixel sorter with the upper limit of the threshold mask set to 1, 0.9, 0.8...0.3. Then, the images generated from this for loop can be stitched together into the frames of a gif. 

The programs I ended up using were primarily [satyarth's pixelsort python module](https://github.com/satyarth/pixelsort/) and [RusticFlare's pixel sort program written in Java](https://github.com/RusticFlare/pixel-sorter). The use of each program is best explained in the documentation, which I've linked.

For combining the frames into a single gif file I used [ezgif](https://ezgif.com/), as it is well, easy. I also made some of the gifs in [ffmpeg](https://ffmpeg.org/), when the file sizes were too large and I didn't want to compress the frames prior to animation.

That's pretty much all there is to it. Making these images was fairly easy as a process but the challenge mostly comes with selecting good images and getting the parameters for the program right to achieve the desired effect.

## other results
&lt;there will be a gallery of images here and explanations as to how i made them here but im still optimizing the files for better web view&gt;

## closing thoughts
Image processing takes a lot of time. I hadn't really thought about it at the time, but if I had scaled down my images before applying the sorting filters I could've experimented with the parameters of the programs much more quickly.

Sometime in the future I think it could be fun to try and implement some of these effects on my own. When I was first starting the project, I had the idea to try and implement them in javascript so that they could be accessible through my site, but I never got around to it.

If you have any questions about this project, reach out! I'd be happy to help anyone with their attempts to reproduce this effect.

## resources
- acerola’s [video](https://www.youtube.com/watch?v=HMmmBDRy-jE) on pixel sorting as a GPU shader effect
- Kim Asendorf’s [code](https://github.com/kimasendorf/ASDFPixelSort/blob/master/ASDFPixelSort.pde)
- satyarth’s [website](http://satyarth.me/articles/pixel-sorting/) and [code](https://github.com/satyarth/pixelsort/)
- RusticFlare’s [code](https://github.com/RusticFlare/pixel-sorter)
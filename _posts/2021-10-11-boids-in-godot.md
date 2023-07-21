---
layout: post
title: making boids in the godot engine
date: 2021-10-11
tags: programming simulations
---
<video controls src="/assets/boids0.mp4" style="margin-top:1em;" muted autoplay loop></video>
These are boids. They are an example of fairly complex behaviors coming from simple rules. They are supposed to be an accurate simulation of flock/schooling behavior that can be observed in birds/fish.

## what rules do boids follow?
There are lots of rules people have made for better boid simulations, but these boids follow the three most common rules:
- boids will try to match the velocity of nearby boids
- boids will move towards the center of mass of nearby boids
- boids will avoid crashing directly into each other

## resources
I looked at a few resources for this project, here they are.
- [Boids Pseudocode](http://www.kfish.org/boids/pseudocode.html)
- [Boids Wikipedia Page](https://en.wikipedia.org/wiki/Boids)
- [Sebastian Lague Boid Coding Adventure](https://www.youtube.com/watch?v=bqtqltqcQhw)
- [Nad Labs Boids in Godot](https://www.youtube.com/watch?v=oFnIlNW_p10)

## view the code on github
You can view the code for this project in its repository on github, [here](https://github.com/spencer-maaaaan/boids).
---
layout: post
title: a barnsley fern rendered in python's matplotlib
date: 2021-04-25
tags: math programming visualizations
---
I saw an interesting post on [/r/factorio](https://www.reddit.com/r/factorio/comments/mumy5x/growing_the_barnsley_fern_in_factorio/) where a user had made a display out of lamps, and used them to plot a Barnsley fern.

Seeing that it could be achieved in Factorio's circuit system, I thought it wouldn't be too hard to try and render a Barnsley Fern in python's popular plotting library, matplotlib. These are the results of those efforts.

<img title="barnsley animation" alt="an animation of a barnsley fern growing" src="/assets/fern.gif" width=300>

## more info
I read a lot for this project, here's a short list of links that I found particularly useful.
- [The wikipedia article on Barnsley ferns](https://en.wikipedia.org/wiki/Barnsley_fern)
- [Python's generator documentation](https://docs.python.org/3/c-api/gen.html)
- [matplotlib's animation documentation](https://matplotlib.org/stable/api/animation_api.html?highlight=animation#module-matplotlib.animation)
- [This matplotlib tutorial which also plots a Barnsley fern](https://scipython.com/book/chapter-7-matplotlib/examples/the-barnsley-fern/)

## view the code on github
You can view the code for this project in its repository on github, [here](https://github.com/spencer-maaaaan/barnsley_fern).
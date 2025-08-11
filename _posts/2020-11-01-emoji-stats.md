---
layout: post
title: emoji stats, a discord bot that tracks emoji use
date: 2020-11-01
tags: programming data
---
A server I'm in makes liberal use of emoji, I thought it would be a neat thing to start collecting data on. It also let me get more familiar with some of Python's built in libraries, like pickle or json.

## example graph
Right now, this is all the bot is capable of outputting, but I'd like to get it to do more sometime possibly.

![A graph of emoji use for a server. The x axis shows emoji names, the y axis shows the number of times each emoji has been used.](/assets/emoji-stats0.webp "sample graph")

## what I'd still like to do with this project but haven't got around to
- show images of the emoji as x labels (including custom emoji)
- change the format that data is stored **again** so that it is easier to make new graph types
- add more types of graphs
    - top users of a particular emoji
    - line chart of an emoji's use over time
    - top emoji for a particular time-frame

## view the code on github
You can view the code for this project in its repository on github, [here](https://github.com/aphex-vim/emoji-stats).
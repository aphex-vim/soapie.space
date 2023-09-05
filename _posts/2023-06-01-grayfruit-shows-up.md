---
layout: post
title: when does grayfruit show up to stream?
date: 2023-06-01
tags: programming data
---
## background
I like to watch a streamer called grayfruit, they are pretty chill and have good taste in games. All of his streams start with a piece of fanart and some music playing while he gets ready. I watch most of grayfruit's streams on his [vod channel](https://www.youtube.com/@fruitsalad5802), and it is customary for someone to post a funny comment that has timestamps to when grayfruit arrives/when the gameplay for the stream starts.

![a youtube comment section. the OP writes, "Grayfruit speaks of dick mountain at 1:48 and starts climbing dick mountain at 5:31." The replies are "This is a pretty good one", "it's always 1:48 isn't it? maybe not always, but definitely the most common", and "god damnit now I want to make a graph."](/assets/gf_comments.png)

The above exchange is from this [video](https://www.youtube.com/watch?v=xevOUqyeTpo), his first stream of _Getting Over It with Bennet Foddy_. Viewing the replies, I was curious -- what time does grayfruit show up to stream, on average?

## process
First I dumped the video IDs of every grayfruit video into one file that I could read from later, I just used [yt-dlp](https://github.com/yt-dlp/yt-dlp) for this as I had some prior experience with it.

Then I signed up for a Google API key, which would let me request the comment data for each video. I wrote a Python script that read the file full of video IDs, and wrote the data for the top 25 comments of each video into a JSON file.

Lastly, I processed the data with another Python script which would find the earliest timestamp in each videos' comments and parsed it into a [timedelta](https://docs.python.org/3/library/datetime.html#timedelta-objects) object, a type for storing an amount of time. Storing the time as a timedelta would make graphing and sorting the times easier down the line.

![a histogram of times. There are peaks at 0:00 and 1:49.](/assets/gf_distribution.png)
## graphing and findings
I decided to only graph datapoints that were &le; 5 minutes, as upon inspection most timestamps later than 5 minutes were mostly not referring to grayfruit's arrival time. This preserves our sample size, bringing the total number of plotted videos from 1474 to 1271.

The graph looks good though, seems like the user from the original thread was pretty much right. Grayfruit's average arrival time is 1:49.75, with a standard deviation of 0:54.95.
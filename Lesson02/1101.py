#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:15:53 2024

@author: hzionn
"""

from pytubefix import YouTube
from pytubefix.cli import on_progress

yt = YouTube(
    # "https://youtu.be/Hax4oTPZ3sA",
    # "https://youtu.be/A5RfSftJRw8",
    "https://www.youtube.com/watch?v=A5RfSftJRw8",
    on_progress_callback=on_progress
)
print(yt.title)

ys = yt.streams.filter(progressive=True)
print(ys)

ys.first().download("")

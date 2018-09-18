#!/usr/bin/python

import os
os.popen('ffmpeg -r 1 -i ./pic/img_%d.jpg video.mp4').read()

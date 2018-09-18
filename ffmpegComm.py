#!/usr/bin/python

import os
os.popen('ffmpeg -r 1 -i /media/sf_602/601/image_%d.jpg video.mp4').read()

import cv2
import sys
import os

from PIL import Image

def calcInterval(Video):
    duration = Video.get(cv2.CAP_PROP_FRAME_COUNT) / Video.get(cv2.CAP_PROP_FPS)
    ratio = len(Video.read()[1]) * 21 / 12000 #Width * 21 / 6 / 2 / 1000
    interval = duration / ratio # Interval to generate frames for ~ 21:6 resolution
  
    return interval

  
def genFrame(Video, interval, count):
  # print "genFrame"
  Video.set(cv2.CAP_PROP_POS_MSEC,(count * interval))
  eov, image = Video.read()
  # print "..."
  return image








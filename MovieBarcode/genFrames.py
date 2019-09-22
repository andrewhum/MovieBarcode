import cv2
import sys
import os

from PIL import Image

def getHeight (movie):
  return len(cv2.VideoCapture(movie).read()[1])

def getWidth (movie):
  return len(cv2.VideoCapture(movie).read()[1][1])

def getInterval(movie):
  vidcap = cv2.VideoCapture(movie)
  duration = vidcap.get(cv2.CAP_PROP_FRAME_COUNT) / vidcap.get(cv2.CAP_PROP_FPS)
  return duration / getWidth(movie) # Interval to generate frames for ~ 21:6 resolution

  
def genFrames(movie, numFrames):
  # print "genFrame"
  vidcap = cv2.VideoCapture(movie)
  image = vidcap.read()[1]
  interval = getInterval(movie)
  frames = []

  for i in range(numFrames):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(i * interval * 1000))
    frames.append(vidcap.read()[1])
    
  return frames
  # print "..."








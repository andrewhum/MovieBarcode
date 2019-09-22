import os
import cv2
import sys
from PIL import Image, ImageDraw
from random import *
import time
import multiprocessing

import genFrames
import avgColour
import drawCode

def main():
  movie = "Files/testVid.mp4"
  title = movie.split("/")[1].split(".")[0]
  print title

  #genFrames
  print "Calculating Interval..."
  vidcap = cv2.VideoCapture(movie)
  interval = genFrames.calcInterval(vidcap)

  print "Drawing Canvas..."
  numFrames = drawCode.drawCanvas(title, movie)

  frames, colours = [], []
  
  print "Generating Frames..."
  for i in range (500):
      frames.append(genFrames.genFrame(vidcap, interval, i))
      #drawCode.drawFrame(avgColour.avgRowCol(frame), count, title)
      #if count == 30: break

  print "Calculating Colours..."
  #p = multiprocessing.Pool(multiprocessing.cpu_count()) 
  p = multiprocessing.Pool(6)
  colours = p.map(avgColour.colArray, frames)

  p.close() 
  p.join()

  print len(colours)


  # img = Image.open("Files/%sCode.jpg" % title)
  # print "Drawing Canvas..."
  # for i in colours:
  #   drawCode.drawFrame(i, count, title)
  #   count += 1

  
  
  print "Number of Frames: ", len(frames)

#########################################################################################################

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
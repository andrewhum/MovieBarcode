import os.path
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

  while True:
    title = raw_input("Movie Title: ")
    movType = raw_input("File Type: ")
    movie = ("Files/%s.%s" % (title, movType))
    if (os.path.exists(movie)): break
    print ("Error 404: File Not Found.")

  width = genFrames.getWidth(movie)
  height = genFrames.getHeight(movie)
  interval = genFrames.calcInterval(movie)

  print ("Movie: ", title)
  print ("Frame Height: ", height)
  print ("Frame Width: ", width)
  #genFrames

  print ("Generating Frames...")
  frames = []
  frames = genFrames.genFrames(movie) #runtime ~4 minutes

  print ("Drawing Canvas...")
  numFrames = drawCode.drawCanvas(title, movie)

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
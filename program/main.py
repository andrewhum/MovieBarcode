import os.path
import cv2
import sys
from PIL import Image, ImageDraw
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
  interval = genFrames.getInterval(movie)

  print ("================================")
  time.sleep(0.5)
  print ("Movie: %s" % title)
  time.sleep(0.5)
  sys.stdout.write ("Frame Dimensions: %d x " % width)
  sys.stdout.write("%d \n" % height)
  time.sleep(0.5)
  print ("================================")
  
  sys.stdout.write("Generating Frames... ")

  frames = []
  frames = genFrames.genFrames(movie, width) #runtime ~4 minutes
  sys.stdout.write("Done. \n")

  sys.stdout.write("Creating Canvas... ")
  drawCode.drawCanvas(movie, width, height)
  sys.stdout.write("Done. \n")

  sys.stdout.write("Calculating Colours... ")
  p = multiprocessing.Pool(6)
  colours = p.map(avgColour.colArray, frames)
  p.close() 
  p.join()
  print len(colours)
  print len(colours[0])
  sys.stdout.write("Done. \n")

  sys.stdout.write("Drawing Barcode... ")
  drawCode.drawFrame(colours)
  sys.stdout.write("Done. \n")

  print ("Complete.")

#########################################################################################################

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
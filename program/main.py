import os
import cv2
import sys
from PIL import Image, ImageDraw
from random import *
import time

import genFrames
import avgColour
import drawCode

#########################################################################################################

""" def main():
    numFrames = genFrames.genFrames('Files/SpiderVerse.mkv')

    print ("Calculating Average Colours...")
    colourArray = avgColour.allColours(1280)
    drawCode.barcode(1280, colourArray)
    print ("Barcode Generated :)")
    print ("Cleaning Files...")

    filelist = [ f for f in os.listdir('Frames')]
    for f in filelist:
      os.remove(os.path.join('Frames', f))

    print ("Program Complete.")

    #print allAvgCols
 """

#########################################################################################################

""" def main():
  movie = "Files/SpiderVerse.mkv"
  count = 0

  title = movie.split("/")[1].split(".")[0]
  print title

  #genFrames
  vidcap = cv2.VideoCapture(movie)
  interval = genFrames.calcInterval(movie)

  drawCode.drawCanvas(1280, title)
  
  while genFrames.genFrame(vidcap, interval, count):
      drawCode.drawFrame(avgColour.avgColour('Frames/frame%d.jpg' % count), count, title)
      print count
      count += 1
      #if count == 20: break
      
  
  print "Number of Frames: ", count

  filelist = [ f for f in os.listdir('Frames')]
  for f in filelist:
    os.remove(os.path.join('Frames', f))
 """
#########################################################################################################

def main():
  movie = "Files/SpiderVerse.mkv"
  count = 0

  title = movie.split("/")[1].split(".")[0]
  print title

  #genFrames
  vidcap = cv2.VideoCapture(movie)
  interval = genFrames.calcInterval(movie)
  
  while genFrames.genFrame(vidcap, interval, count):
      if count == 0: drawCode.drawCanvas(1280, title)
      drawCode.drawFrame(avgColour.avgRowCol('Frames/frame%d.jpg' % count), count, title)
      print count
      count += 1
      #if count == 30: break
      
  
  print "Number of Frames: ", count

  filelist = [ f for f in os.listdir('Frames')]
  for f in filelist:
    os.remove(os.path.join('Frames', f))

#########################################################################################################

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

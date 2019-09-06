import urllib2 
import cv2
import sys
import os
import time

from PIL import Image
import multiprocessing

def calcInterval(Video):
    duration = Video.get(cv2.CAP_PROP_FRAME_COUNT) / Video.get(cv2.CAP_PROP_FPS)
    ratio = len(Video.read()[1]) * 21 / 6000
    interval = duration / ratio # Interval to generate frames for ~ 21:6 resolution
  
    return interval

  
def genFrame(Video, interval, count):
  # print "genFrame"
  Video.set(cv2.CAP_PROP_POS_MSEC,(count * interval))
  eov, image = Video.read()
  # print "..."
  return image

    
def avgRowCol(frame):
    rowCol = []
    for i in range(len(frame)):
        avgr, avgg, avgb = 0, 0, 0
        for j in range(len(frame[0])):
            avgr += frame[i][j][2]
            avgg += frame[i][j][1]
            avgb += frame[i][j][0]
        rgbRow = (avgr / len(frame[0]), avgg / len(frame[0]), avgb / len(frame[0]))
        rowCol.append(rgbRow)           
    return rowCol 

def main():

    movie = "Files/testVid.mp4"
    vidcap = cv2.VideoCapture(movie)
    interval = calcInterval(vidcap)
    frames = []

    print multiprocessing.cpu_count()

    print "Generating Frames"

    for i in range(20):
        frames.append(genFrame(vidcap, 3000, i)) #3000 gets roughly 20 scenes

    start_time = time.time()
    p = multiprocessing.Pool(6) 
    results = p.map(genFrame, vidcap, 3000, 20)

    p.close() 
    p.join() 

    print("--- %s seconds ---" % (time.time() - start_time))

    # start_time = time.time()
    
    # p = multiprocessing.Pool(6) 
    # results = p.map(avgRowCol, frames)

    # p.close() 
    # p.join() 

    # print("--- %s seconds ---" % (time.time() - start_time))


main()

import cv2
import sys
import os

from PIL import Image

#########################################################################################################

""" def genFrames(movie):

  #os.makedirs('Frames')

  vidcap = cv2.VideoCapture(movie)
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
  duration = int(frame_count / fps)
  
  # print ("genFrames fps: ", fps)
  # print ("genFrames frame_count: ", frame_count)
  # print ("genFrames duration: ", duration)

  vidcap.release()

  interval = duration / 1.28 # 1280 frames / 1000 

  vidcap = cv2.VideoCapture(movie)
  success,image = vidcap.read()
  count = 0
  success = True

  while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count * interval)) # captures frame every interval
    cv2.imwrite('Frames/frame%d.jpg' % count, image)     # save frame as JPEG file
    success,image = vidcap.read()
    count += 1
    # sys.stdout.write("=")
    # sys.stdout.flush()
    # if (count % 3 == 0): sys.stdout.write("Generating Frames ...")
    # elif (count % 2 == 0): sys.stdout.write("Generating Frames ..")
    # sys.stdout.write("Generating Frames")
    # os.system('cls' if os.name == 'nt' else 'clear')

  sys.stdout.write("]\n")
  print "Successfully generated ", count, "frames. "
  return count 

def main():
  genFrames('Files/SpiderVerse.mkv')

main() """

#########################################################################################################

""" def calcInterval(movie):
  vidcap = cv2.VideoCapture(movie)
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  frame_count = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
  duration = frame_count / fps

  # print "genFrames fps: ", fps
  # print "genFrames frame_count: ", frame_count
  # print "genFrames duration: ", duration

  vidcap.release()

  interval = duration / 1.9 # Interval to generate 1280 Frames

  return interval

def genFrame(vidcap, interval, count):
  success,image = vidcap.read()
  success = True

  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count * interval)) # captures frame every interval
  cv2.imwrite('Frames/frame%d.jpg' % count, image)     # save frame as JPEG file
  success,image = vidcap.read()

  return success """


#########################################################################################################


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

""" def main():
  vidcap = cv2.VideoCapture("Files/testVid.mp4")
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  print fps
  frame_count = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
  print frame_count
  duration = frame_count / fps
  
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(21540))
  # image = vidcap.read()[1]

  # print image[0][0][2] # R value
  # print image[0][0][1] # G value
  # print image[0][0][0] # B value

  print genFrame(vidcap)

main() """


""" def main():
  movie = "Files/testVid.mp4"
  vidcap = cv2.VideoCapture(movie)
  interval = calcInterval(vidcap)
  print genFrame(vidcap, interval, 0)

main() """

#########################################################################################################








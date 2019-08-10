import cv2
import sys
import os

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

#def main():
#  genFrames('Files/SpiderVerse.mkv')

#main() """

#########################################################################################################

def calcInterval(movie):
  vidcap = cv2.VideoCapture(movie)
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  frame_count = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
  duration = frame_count / fps

  # print "genFrames fps: ", fps
  # print "genFrames frame_count: ", frame_count
  # print "genFrames duration: ", duration

  vidcap.release()

  interval = duration / 1.28 # Interval to generate 1280 Frames

  return interval

def genFrame(vidcap, interval, count):
  success,image = vidcap.read()
  success = True

  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count * interval)) # captures frame every interval
  cv2.imwrite('Frames/frame%d.jpg' % count, image)     # save frame as JPEG file
  success,image = vidcap.read()

  return success

# def main():
#   movie = "Files/SpiderVerse.mkv"
#   vidcap = cv2.VideoCapture(movie)
#   interval = calcInterval(movie)
#   genFrame(vidcap, interval, 0)

# main()

#########################################################################################################








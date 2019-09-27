from PIL import Image
import sys

def colArray(frame):
  colours = []


  for i in range(0, len(frame), 2): # len(frame) = 720
    avgr, avgg, avgb = 0, 0, 0
    for j in range (0, len(frame[0]), len(frame[0]) / 10): # len(frame[0]) = 1280
      avgr += frame[i][j][2]
      avgg += frame[i][j][1]
      avgb += frame[i][j][0]
    rgbRow = (avgr / 10, avgg / 10, avgb / 10)
    colours.append(rgbRow) 

  return colours
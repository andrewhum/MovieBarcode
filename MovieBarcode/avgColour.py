from PIL import Image
import sys

import genFrames

width = 10

def colArray(frame):
    colours = []
    for i in range(0, global width, 2):
        avgr, avgg, avgb = 0, 0, 0
        for j in range (0, len(frame[0]), 2):
            avgr += frame[i][j][2]
            avgg += frame[i][j][1]
            avgb += frame[i][j][0]
        rgbRow = (avgr / len(frame[0]), avgg / len(frame[0]), avgb / len(frame[0]))
        colours.append(rgbRow) 

    return colours
import cv2
import sys
from PIL import Image, ImageDraw
from random import *


def drawCanvas(movie, w, h):
    frame = cv2.VideoCapture(movie).read()[1]
    img = Image.new('RGB', (w, h / 2), (255, 255, 255))
    img.save("Files/BarCode.jpg", "PNG")

def drawFrame(colours):
    img = Image.open("Files/BarCode.jpg")
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = colours[i][j]

    img.save("Files/BarCode.jpg")
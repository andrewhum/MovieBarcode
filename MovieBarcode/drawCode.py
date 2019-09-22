import cv2
from PIL import Image, ImageDraw
from random import *

def drawCanvas(title, movie):
    vidcap = cv2.VideoCapture(movie)
    frame = vidcap.read()[1]
    img = Image.new('RGB', (len(frame) * 21 / 12, len(frame) / 2), (255, 255, 255))
    img.save("Files/%sBarCode.jpg" % title, "PNG")
    return (len(frame) / 12 * 21)
    

def drawFrame(colour, count, title):
    img = Image.open("Files/%sBarCode.jpg" % title)
    pixels = img.load()
    for i in range(img.size[1]):
        pixels[count, i] = colour[i]

    img.save("Files/%sBarCode.jpg" % title)
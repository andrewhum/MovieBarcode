import cv2
from PIL import Image, ImageDraw
from random import *

#########################################################################################################

""" def barcode(numFrames, rgbArray):

    img = Image.new('RGB', (numFrames, int(numFrames / 18.0 * 5.0)), (255, 255, 255))
    img.save("Files/canvas.jpg", "PNG")

    img = Image.open("Files/canvas.jpg")

    print "Image Size is", img.size[0], " x ", img.size[1]

    draw = ImageDraw.Draw(img)
    for i in range(numFrames):
        draw.line((i, 0, i, img.size[1]) , fill = rgbArray[i], width = 1)

    img.save("Files/canvas.jpg") """

#########################################################################################################

""" def drawCanvas(numFrames, title):
    img = Image.new('RGB', (numFrames, int(numFrames / 18.0 * 5.0)), (255, 255, 255))
    img.save("Files/%sBarCode.jpg" % title, "PNG")

def drawFrame(colour, count, title):
    img = Image.open("Files/%sBarcode.jpg" % title)

    draw = ImageDraw.Draw(img)
    draw.line((count, 0, count, img.size[1]), fill = colour, width = 1)
    img.save("Files/%sBarCode.jpg" % title) """

#########################################################################################################

""" def drawCanvas(title):
    frame = Image.open("Frames/frame0.jpg", 'r')
    img = Image.new('RGB', (frame.size[0], frame.size[1]), (255, 255, 255))
    img.save("Files/%sBarCode111.jpg" % title, "PNG")
    

def drawFrame(colour, count, title):
    img = Image.open("Files/%sBarcode111.jpg" % title)
    pixels = img.load()

    for i in range(img.size[1]):
        pixels[count, i] = colour[i]

    img.save("Files/%sBarCode111.jpg" % title)
 """

#########################################################################################################

def drawCanvas(title, movie):
    vidcap = cv2.VideoCapture(movie)
    frame = vidcap.read()[1]
    img = Image.new('RGB', (len(frame) * 21 / 12, len(frame)), (255, 255, 255))
    img.save("Files/%sCode.jpg" % title, "PNG")
    return (len(frame) / 12 * 21)
    

def drawFrame(colour, frame, title):
    img = Image.open("Files/%sCode.jpg" % title)
    pixels = img.load()

    for i in range(img.size[1]):
        pixels[frame, i] = colour[i]

    img.save("Files/%sCode.jpg" % title)
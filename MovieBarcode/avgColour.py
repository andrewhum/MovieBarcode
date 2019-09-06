from PIL import Image
import sys

#########################################################################################################

""" def avgColour(file):
        frame = Image.open(file, 'r')
        pixel = frame.load()
        pixr, pixg, pixb = [], [], []
        avgr, avgg, avgb = 0, 0, 0

        for i in range(frame.size[0]):
                for j in range(frame.size[1]):
                        avgr += pixel[i, j][0]
                        avgg += (pixel[i, j][1])
                        avgb += (pixel[i, j][2])

        avgr = avgr / (frame.size[0] * frame.size[1])
        avgg = avgg / (frame.size[0] * frame.size[1])
        avgb = avgb / (frame.size[0] * frame.size[1])

        avgColour = (avgr, avgg, avgb)

        return avgColour

def allColours(numFrames):
        allAvgCols = []

        #sys.stdout.write("Calculating Frames Average Colours: ")
        #sys.stdout.write("[")
        #sys.stdout.flush()
        
        for i in range(numFrames):
                allAvgCols.append(avgColour('Frames/frame%d.jpg' % i))
                #sys.stdout.write("=")
                #sys.stdout.flush()

        #sys.stdout.write("]\n")

        # print allAvgCols

        return allAvgCols """

#########################################################################################################
#########################################################################################################

""" def avgColour(frame):
        img = Image.open(frame, 'r')
        pixel = img.load()
        pixr, pixg, pixb = [], [], []
        avgr, avgg, avgb = 0, 0, 0

        for i in range(img.size[0]):
                for j in range(img.size[1]):
                        avgr += pixel[i, j][0]
                        avgg += (pixel[i, j][1])
                        avgb += (pixel[i, j][2])

        avgr = avgr / (img.size[0] * img.size[1])
        avgg = avgg / (img.size[0] * img.size[1])
        avgb = avgb / (img.size[0] * img.size[1])

        avgColour = (avgr, avgg, avgb)

        return avgColour """

#########################################################################################################

""" def avgRowCol(frame):
        img = Image.open(frame, 'r')
        pixel = img.load()
        pixr, pixg, pixb = [], [], []
        rowCol = []


        for j in range(img.size[1]):
                avgr, avgg, avgb = 0, 0, 0
                for i in range(img.size[0]):
                        avgr += pixel[i, j][0]
                        avgg += (pixel[i, j][1])
                        avgb += (pixel[i, j][2])
                rgbRow = (avgr / img.size[0], avgg / img.size[0], avgb / img.size[0])  
                rowCol.append(rgbRow)           

        return rowCol 
 """
#########################################################################################################

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


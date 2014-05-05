# standard libraries to import
import os, sys, fixelFunctions

# create variables for the system to iterate through
inputImages = list(sys.argv)[1:]
inputImageCount = 1

# create variables for each image
thisModule = sys.modules[__name__]
for currentImage in inputImages:
	setattr(thisModule,"image"+str(inputImageCount),[fixelFunctions.imageData(currentImage),fixelFunctions.imageLoad(currentImage),currentImage])
	inputImageCount += 1

############
# begin fixel script

def generateWallpaper(imageName,desktopWidth,desktopHeight):
	fixelFunctions.grayscale(imageName)
	fixelFunctions.stretch(imageName,desktopWidth,desktopHeight)
	fixelFunctions.caption(imageName,"Welcome to My Computer!")
	
red = fixelFunctions.color(0,34,55)
image1[1][2,4] = red

# end fixel script
############

# output the final images
outputImageCount = 1
for currentImage in inputImages:
	fixelFunctions.saveImage(getattr(thisModule,"image"+str(outputImageCount)),"JPEG")
	outputImageCount += 1
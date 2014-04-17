# standard libraries to import
import os, sys, fixelFunctions

# create variables for the system to iterate through
outputImages = list(sys.argv)
del outputImages[0]
outputImageCount = 0

# set attributes of each file using setattr for attr value in vars(namespace).itteritem():
# setattr(client,attr,value)

# create a variable containing the raw image data for the input images
for currentImage in outputImages:
	outputImages[outputImageCount] = fixelFunctions.imageData(currentImage)
	outputImageCount = outputImageCount+1

# begin the custom functions here
# perform any necessary transformations to the input images (as per the fixel script
grayscale(image1);
outputImages[0] = fixelFunctions.caption(outputImages[0],"testing this outtt","wj")

# output all images with "-fixel" appended to the end
inputImages = list(sys.argv)
del inputImages[0]
inputImageCount = 0
for currentImage in inputImages:
	fixelFunctions.saveImage(outputImages[inputImageCount],os.path.splitext(currentImage)[0],"JPEG")
	inputImageCount = inputImageCount+1
	



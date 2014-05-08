import os
import sys
import fixelFunctions

inputImages = sys.argv[1:]
inputImageCount = 0
Namespace = type('Namespace', (object,), {'images': []})  # cleaner than having to declare a class
ns = Namespace()

# create variables for each image
for currentImage in inputImages:
	image = [fixelFunctions.imageData(currentImage), fixelFunctions.imageLoad(currentImage), currentImage]
	setattr(ns, "image"+str(inputImageCount), image)
	ns.images.append(image)
	inputImageCount += 1
	
images = [ns.image0, ns.image1, ns.image2, ns.image3]
fixelFunctions.collage(ns.image1, images, 1600, 1200)

for image in ns.images:
	fixelFunctions.saveImage(image, "JPEG")
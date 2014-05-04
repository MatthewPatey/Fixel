def create_program(main_string, functions_string):
	return imports + functions_string + main_pre_fixel + main_string + main_post_fixel


imports = '''\
\'\'\'
  ______   __     __  __     ______     __        
 /\  ___\ /\ \   /\_\_\_\   /\  ___\   /\ \       
 \ \  __\ \ \ \  \/_/\_\/_  \ \  __\   \ \ \____  
  \ \_\    \ \_\   /\_\/\_\  \ \_____\  \ \_____\ 
   \/_/     \/_/   \/_/\/_/   \/_____/   \/_____/ 
                                                     
\'\'\'

import sys
from py import fixelFunctions

'''


main_pre_fixel = '''
inputImages = sys.argv[1:]
inputImageCount = 1
Namespace = type('Namespace', (object,), {})  # cleaner than having to declare a class
ns = Namespace()
ns.images = []

# create variables for each image
for currentImage in inputImages:
	image = [fixelFunctions.imageData(currentImage), currentImage]
	setattr(ns, "image"+str(inputImageCount), image)
	ns.images.append(image)
	inputImageCount += 1
'''

main_post_fixel = '''
for outputImageCount in range(1, len(inputImages)+1):
	fixelFunctions.saveImage(getattr(ns, "image"+str(outputImageCount)), "JPEG")
'''

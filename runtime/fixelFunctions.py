import os
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageDraw

def imageData(infile):
	return Image.open(infile)
	
def imageLoad(indata):
	return indata.load()
	
def saveImage(indata,filetype):
	outfile = os.path.splitext(indata.name)[0] + "-fixel.jpg"
	indata.image_data.convert('RGB').save(outfile,filetype)

def grayscale(indata):
	im = indata.image_data.convert("L").convert("RGB")
	indata.set_image_data(im)

def scale(indata,ratio):
	im = indata.image_data
	size = im.size[0]*ratio,im.size[1]*ratio
	im = im.resize(size, Image.ANTIALIAS)
	indata.set_image_data(im)

def stretch(indata,newWidth,newHeight):
	im = indata.image_data
	size = newWidth,newHeight
	newIm = im.resize(size, Image.ANTIALIAS)
	indata.set_image_data(newIm)

def rotate(indata,angle):
	im = indata.image_data.convert('RGBA')
	rot = im.rotate(22.2, expand=1)
	white = Image.new('RGBA', rot.size, (255,)*4)
	im = Image.composite(rot, white, rot)
	im.convert(indata.image_data.mode)
	indata.set_image_data(im)
		
def overlay(indata,rgb,opacity):
	opacity = int(255*float(opacity)/100)	
	rgb.append(opacity)
	rgb=tuple(rgb)
	im = indata.image_data
	overlayColor = Image.new(mode='RGBA',size=im.size,color=rgb)
	im.paste(overlayColor, [0,0,im.size[0],im.size[1]], overlayColor)
	indata.set_image_data(im)

def blur(indata,degree):
	if (degree>10):
		degree = 10
	elif (degree<0):
		degree=0
	im = indata.image_data.filter(fixelGaussianBlur(radius=degree))
	indata.set_image_data(im)

def sharpen(indata,degree):
	if (degree>10):
		degree = 10
	elif (degree<0):
		degree=0
	im = ImageEnhance.Sharpness(indata.image_data).enhance(degree)
	indata.set_image_data(im)
	
def brighten(indata,degree):
	degree=(degree/10)+1
	if (degree>2):
		degree = 2
	elif (degree<0):
		degree=0
	im = ImageEnhance.Brightness(indata.image_data).enhance(degree)
	indata.set_image_data(im)

def contrast(indata,degree):
	degree=(degree/10)+1
	if (degree>2):
		degree = 2
	elif (degree<0):
		degree=0
	im = ImageEnhance.Contrast(indata.image_data).enhance(2)
	indata.set_image_data(im)
	
def border(indata,border,color):
	im = ImageOps.expand(indata.image_data,border=border,fill=color)
	indata.set_image_data(im)

def cropit(indata,coordinates):
	im = indata.image_data.crop(coordinates)
	indata.set_image_data(im)
	
def caption(indata,text):
	font_file_path = os.path.join(os.path.dirname(__file__), "HelveticaNeue.ttc")
	font = ImageFont.truetype(font_file_path, 100)
	im = ImageDraw.Draw(indata.image_data)
	im.text((10, 10), text, fill="#ff0000", font=font)
	del im
	
def color(r,g,b):
	return (r,g,b,0)

class fixelGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"
    
    def __init__(self, radius=2):
        self.radius = radius
    
    def filter(self, image):
        return image.gaussian_blur(self.radius)
	
class fixelGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"
    
    def __init__(self, radius=2):
        self.radius = radius
    
    def filter(self, image):
        return image.gaussian_blur(self.radius)

import os, sys
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageDraw

def imageData(infile):
	return Image.open(infile)
	
def saveImage(indata,infile,filetype):
	outfile = infile + "-fixel.jpg"
	indata.save(outfile,filetype)

def grayscale(indata):
	im = indata.convert("L")
	return im



def scale(indata,ratio):
	im = indata
	size = im.size[0]*ratio,im.size[1]*ratio
	im.resize(size, Image.ANTIALIAS)
	return im

def rotate(indata,angle):
	im = indata.convert('RGBA')
	rot = im.rotate(22.2, expand=1)
	white = Image.new('RGBA', rot.size, (255,)*4)
	im = Image.composite(rot, white, rot)
	im.convert(indata.mode)
	return im
		
def overlay(indata,rgb,opacity):
	opacity = int(255*float(opacity)/100)	
	rgb.append(opacity)
	rgb=tuple(rgb)
	im = indata
	overlayColor = Image.new(mode='RGBA',size=im.size,color=rgb)
	im.paste(overlayColor, [0,0,im.size[0],im.size[1]], overlayColor)
	return im

def blur(indata,degree):
	if (degree>10):
		degree = 10
	elif (degree<0):
		degree=0
	im = indata.filter(fixelGaussianBlur(radius=blurDegree))
	return im
	
def sharpen(indata,degree):
	if (degree>10):
		degree = 10
	elif (degree<0):
		degree=0
	im = ImageEnhance.Sharpness(indata).enhance(degree)
	return im
	
def brighten(indata,degree):
	degree=(degree/10)+1
	if (degree>2):
		degree = 2
	elif (degree<0):
		degree=0
	im = ImageEnhance.Brightness(indata).enhance(degree)
	return im

def contrast(indata,degree):
	degree=(degree/10)+1
	if (degree>2):
		degree = 2
	elif (degree<0):
		degree=0
	im = ImageEnhance.Contrast(indata).enhance(2)
	return im
	
def border(indata,border,color):
	im = ImageOps.expand(indata,border=border,fill=color)
	return im

def cropit(indata,coordinates):
	im = indata.crop(coordinates)
	return im
	
def caption(indata,text,formatting):
	font = ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.dfont",400)
	im = ImageDraw.Draw(indata)
	im.text((10, 10), text, fill='red', font=font)
	del im
	return indata
	
class fixelGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"
    
    def __init__(self, radius=2):
        self.radius = radius
    
    def filter(self, image):
        return image.gaussian_blur(self.radius)
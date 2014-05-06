import os, sys
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageDraw

def imageData(infile):
	return Image.open(infile)
	
def imageLoad(infile):
	im = Image.open(infile)
	return im.load()
	
def saveImage(indata,filetype):
	outfile = os.path.splitext(indata[2])[0] + "-fixel.jpg"
	indata[0].convert('RGB').save(outfile,filetype)

def grayscale(indata):
	im = indata[0].convert("L").convert("RGB")
	indata[0] = im
	
def scale(indata,ratio):
	im = indata[0]
	size = im.size[0]*ratio,im.size[1]*ratio
	im.resize(size, Image.ANTIALIAS)
	indata[0] = im

def stretch(indata,newWidth,newHeight):
	im = indata[0]
	size = newWidth,newHeight
	newIm = im.resize(size, Image.ANTIALIAS)
	indata[0] = newIm

def rotate(indata,angle):
	im = indata.convert('RGBA')
	rot = im.rotate(22.2, expand=1)
	white = Image.new('RGBA', rot.size, (255,)*4)
	im = Image.composite(rot, white, rot)
	im.convert(indata.mode)
	indata[0] = im
		
def overlay(indata,rgb,opacity):
	opacity = int(255*float(opacity)/100)	
	rgb.append(opacity)
	rgb=tuple(rgb)
	im = indata[0]
	overlayColor = Image.new(mode='RGBA',size=im.size,color=rgb)
	im.paste(overlayColor, [0,0,im.size[0],im.size[1]], overlayColor)
	indata[0] = im

def blur(indata,degree):
	if (degree>10):
		degree = 10
	elif (degree<0):
		degree=0
	im = indata[0].filter(fixelGaussianBlur(radius=blurDegree))
	indata[0] = im
	
def sharpen(indata,degree):
	if (degree>10):
		degree = 10
	elif (degree<0):
		degree=0
	im = ImageEnhance.Sharpness(indata[0]).enhance(degree)
	indata[0] = im
	
def brighten(indata,degree):
	degree=(degree/10)+1
	if (degree>2):
		degree = 2
	elif (degree<0):
		degree=0
	im = ImageEnhance.Brightness(indata[0]).enhance(degree)
	indata[0] = im

def contrast(indata,degree):
	degree=(degree/10)+1
	if (degree>2):
		degree = 2
	elif (degree<0):
		degree=0
	im = ImageEnhance.Contrast(indata[0]).enhance(2)
	indata[0] = im
	
def border(indata,border,color):
	im = ImageOps.expand(indata[0],border=border,fill=color)
	indata[0] = im

def cropit(indata,coordinates):
	im = indata[0].crop(coordinates)
	indata[0] = im
	
def caption(indata,text):
	font_file_path = os.path.join(os.path.dirname(__file__), "HelveticaNeue.ttc")
	font = ImageFont.truetype(font_file_path, 100)
	im = ImageDraw.Draw(indata[0])
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

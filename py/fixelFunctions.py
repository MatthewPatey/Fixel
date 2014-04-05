import os, sys
import Image, ImageDraw

def imageData(infile):
	return Image.open(infile)
	
def saveImage(indata,infile,filetype):
	outfile = infile + "-fixel.jpg"
	indata.save(outfile,filetype)

def grayscale(indata):
	im = indata.convert("L")
	return im
		
def overlay(indata,rgb,opacity):
	opacity = int(255*float(opacity)/100)	
	rgb.append(opacity)
	rgb=tuple(rgb)
	im = indata
	overlayColor = Image.new(mode='RGBA',size=im.size,color=rgb)
	im.paste(overlayColor, [0,0,im.size[0],im.size[1]], overlayColor)
	return im
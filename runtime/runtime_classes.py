from runtime fixelFunctions


class Image:
	def __init__(self, name):
		self.name = name
		self.image_data = fixelFunctions.imageData(name)
		self.pixel_data = fixelFunctions.imageLoad(name)
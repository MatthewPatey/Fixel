from runtime import fixelFunctions



class Image(object):
	def __init__(self, name):
		self.name = name
		self.image_data = fixelFunctions.imageData(name)
		self.pixel_data = None

	def __getattr__(self, item):
		if item == 'width':
			return getattr(self.image_data, 'size')[0]
		elif item == 'height':
			return getattr(self.image_data, 'size')[1]

	def __getitem__(self, index):
		self.load_pixel_data_if_needed()
		return self.pixel_data[index]

	def __setitem__(self, index, value):
		self.load_pixel_data_if_needed()
		self.pixel_data[index] = value

	def load_pixel_data_if_needed(self):
		if self.pixel_data is None:
			self.pixel_data = fixelFunctions.imageLoad(self.image_data)

	def set_image_data(self, new_image_data):
		self.image_data = new_image_data
		self.pixel_data = None


class Pixel:
	pass

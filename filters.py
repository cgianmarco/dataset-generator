from trasformer import * 

# string -> string
class capitalizedTrasformer(Trasformer):

	def trasform_single(self, value):
		return value.capitalize()


# string -> string
class swapcaseTrasformer(Trasformer):

	def trasform_single(self, value):
		return value.swapcase()


# string -> string
class uppercaseTrasformer(Trasformer):

	def trasform_single(self, value):
		return value.upper()


# string -> string
class capitalSTrasformer(Trasformer):

	def trasform_single(self, value):
		return value.replace('s', 'S')


# image -> image
class verticalFlipTrasformer(Trasformer):

	def trasform_single(self, value):
		return value.transpose(Image.FLIP_TOP_BOTTOM)


# image -> image
class horizontalFlipTrasformer(Trasformer):

	def trasform_single(self, value):
		return value.transpose(Image.FLIP_LEFT_RIGHT)


# image -> image array
class douleImageTrasformer(Trasformer):

	def trasform_single(self, value):
		return [value, value.copy()]


# image -> image
class removeWhiteBackgroundTrasformer(Trasformer):

	def trasform_single(self, value):
		img = value.convert("RGBA")

		pixdata = img.load()

		for y in xrange(img.size[1]):
		    for x in xrange(img.size[0]):
		        if pixdata[x, y] == (255, 255, 255, 255):
		            pixdata[x, y] = (255, 255, 255, 0)
		return img
				

# image -> image
class addBackgroundTrasformer(Trasformer):

	def __init__(self, background):
		self.background = background

	def trasform_single(self, value):
		img = self.background.copy()
		img.paste(value, (0, 0), value)
		return img 

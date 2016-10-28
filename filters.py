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
		print "eseguito"
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


# image -> image array
class addBackgroundAllPositionsTrasformer(Trasformer):

	def __init__(self, background, step):
		self.background = background
		self.step = step

	def trasform_single(self, value):
		x = 0
		y = 0

		results = []
		while x <= (self.background.width - value.width):
			# print "x = " + str(x)
			y = 0
			while y <= (self.background.height - value.height):
				# print "y = " + str(y)
				img = self.background.copy()				
				img.paste(value, (x, y), value)
				results.append(img.copy())
				y = y + self.step	
			x = x + self.step
		return results


# image -> image array
class addBackgroundRandomPositionsTrasformer(Trasformer):

	def __init__(self, background, n):
		self.background = background
		self.n = n

	def trasform_single(self, value):
		import random

		results = []

		for i in range(self.n):
			x = random.randint(0, self.background.width - value.width)
			y = random.randint(0, self.background.height - value.height)
			img = self.background.copy()				
			img.paste(value, (x, y), value)
			results.append(img.copy())

		return results


# image -> image array
class RotateTrasformer(Trasformer):

	def __init__(self, max_angle):
		self.max_angle = max_angle

	def trasform_single(self, value):

		angle = 0

		results = []
		while angle <= self.max_angle:
			img = value.copy()				
			img = img.rotate(angle)
			results.append(img)
			angle = angle + 10
		return results

		

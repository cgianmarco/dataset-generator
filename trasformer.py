#coding=utf-8

import Image
import numpy as np


"""
 Every filter must extend this class

"""
class Trasformer:

	def trasform(self, value):
		res = []
		for x in value:
			if isinstance(self.trasform_single(x), list):
				res.extend(self.trasform_single(x))
			else:
				res.append(self.trasform_single(x))
		return res


	def trasform_single(self, value):
		raise NotImplementedError("Trasform function not implemented")

	def then(self, t):

		class recursiveTrasformer(Trasformer):

			def __init__(self, parent, child):
				self.parent = parent
				self.child = child

			def trasform(self, value):
				return self.child.trasform(self.parent.trasform(value))

		return recursiveTrasformer(self, t)



class CompositeTrasformer(Trasformer):

	def __init__(self, *trasformers):

		self.trasformers = trasformers


	def trasform(self, value):

		partialResults = []
		results = []

		partialResults.append(value)
		results.extend(value)

		for trasformer in self.trasformers:
			res = []
			for v in partialResults:
				res.extend(trasformer.trasform(v))
			results.extend(res)
			partialResults.append(res)
		# print partialResults
		return results


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


# image -> 2d image array
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



"""
 Execute filter on given value
 
"""
def execute(value, t):
	results = t.trasform(value)
	return results


"""
 Show input images and output images of trasformer

 WORK IN PROGRESS!

"""
def test(img, trasformer):
	from matplotlib import pyplot as plt
	processed_img = execute(img, trasformer)
	plt.subplot(311),plt.imshow(img[0],'gray'),plt.title('ORIGINAL')
	print len(processed_img)
	plt.subplot(312),plt.imshow(processed_img[0],'gray'),plt.title('TRASFORMED')
	plt.subplot(313),plt.imshow(processed_img[1],'gray'),plt.title('TRASFORMED')
	# plt.subplot(234),plt.imshow(processed_img[2],'gray'),plt.title('TRASFORMED')
	# plt.subplot(235),plt.imshow(processed_img[3],'gray'),plt.title('TRASFORMED')
	plt.show()





img = Image.open("contattaci.png").convert('RGBA')
img2 = Image.open("iphone.png").convert('RGBA')
background = Image.open("test.jpg").convert('RGBA')


images = [img, img2]

trasformer = CompositeTrasformer(horizontalFlipTrasformer(), verticalFlipTrasformer())
trasformer = removeWhiteBackgroundTrasformer().then(douleImageTrasformer())


test(images, trasformer)





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












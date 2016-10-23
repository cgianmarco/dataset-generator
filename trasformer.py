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
			result = self.trasform_single(x)
			if isinstance(result, list):
				res.extend(result)
			else:
				res.append(result)
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












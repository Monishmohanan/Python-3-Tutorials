# For loop working in python
'''
iter_obj = iter(iterable)

while True:
	try:
		element = next(iter_obj)
	except StopIteration:
		break
'''

# Building your own iterator in python

class PowTwo:
	"""Class to implement an iterator of the powers of two"""
	def __init__(self, max = 0):
		self.max = max

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n <= self.max:
			result = 2 ** self.n
			self.n += 1
			return result
		else:
			raise StopIteration
'''
for i in PowTwo(5):
	print(i)
'''
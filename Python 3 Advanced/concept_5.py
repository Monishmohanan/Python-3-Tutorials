# some behaviour I wanted to implement >> write some __function__ (Dunder methods or Data model methods)
# top-level function or top-level syntax >> corresponding __
class Polynomial:
	def __init__(self, *coeffs):
		self.coeffs = coeffs

	def __repr__(self):
		return 'Polynomial(*{!r})'.format(self.coeffs)

	def __add__(self, others):
		return Polynomial(*(x+y for x, y in zip(self.coeffs, others.coeffs)))

	def __len__(self):
		return len(self.coeffs)


p1 = Polynomial(1, 3, 4)
p2 = Polynomial(2, 4, 6)
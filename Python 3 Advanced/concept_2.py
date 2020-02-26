class Person:
	def __init__(self, name):
		self.name = name

	#adding a data model method or dunder method
	def __repr__(self):
		return f"Person({self.name})"

	def __mul__(self, x):
		if type(x) is not int:
			raise Exception("Invalid arguement, must be int")

		self.name = self.name * x

	def __call__(self, y):
		print("called this function: ",y)

	def __len__(self):
		return len(self.name)

p = Person("Monish")
#p * 4
#p(4)
#print(p)
print(len(p))
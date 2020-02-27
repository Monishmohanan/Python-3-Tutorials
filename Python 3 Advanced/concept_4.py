# META CLASSES

'''
class Meta(type):
	def __new__(self, class_name, bases, attrs):    # modifies the construction of the object. gets called before init
		print(attrs)
		
		return type(class_name, bases, attrs)

class Dog(metaclass = Meta):
	x = 5
	y = 8

	def hello(self):
		print("hi")   # without even instantiating the class gets constructed

'''

class Meta(type):
	def __new__(self, class_name, bases, attrs):
		print(attrs)

		#changing the attributes

		a = {}

		for name, val in attrs.items():
			if name.startswith("__"):
				a[name] = val
			else:
				a[name.upper()] = val

		print(a)
		return type(class_name, bases, a)

class Dog(metaclass = Meta):
	x = 5
	y = 8

	def hello(self):
		print("hi")

# proof for the change of attributes

d = Dog()
#print(d.x)   # wont work since attributes are changed
print(d.X)

#print(d.hello())  # wont work since the attributes are changed
print(d.HELLO())



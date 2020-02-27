# META CLASSES 

# create classes using type
Test = type("Test", (), {"x":5})    #type(name, basis or parent class(must be a tuple), attribute)
t = Test()
print(t.x)
t.wy = "hello"
print(t.wy)


class Foo:
	def show(self):
		print("hi")


def add_attribute(self):
	self.z = 9


new = type('new', (Foo,), {"x":5, "add_attribute":add_attribute})
m = new()
m.add_attribute()
print(m.z)
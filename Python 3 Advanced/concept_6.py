# Decorators - generally used to validate input in our code
'''
def func(f):
	def wrapper(*args, **kwargs):
		print("started")
		rv = f(*args, **kwargs)
		print("ended")
		return rv
	return wrapper

@func
def func2():
	print("I am func2")

@func
def func3(x, y):
	print("I am func3")
	print(x)
	return y


func2()
x = func3(3, 5)
print(x)

'''

import time

def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		rv = func()
		total = time.time() - start
		print("Time: ", total)
		return rv

	return wrapper

@timer
def test():
	for _ in range(1000):
		pass

@timer
def test2():
	time.sleep(2)

test()
test2()
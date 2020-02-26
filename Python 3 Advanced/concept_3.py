from queue import Queue
import inspect

q = Queue()
print(q)

print(inspect.getsource(Queue))

#create a customised class inherited from a standard class using the dunder methods/ data models
"""
from queue import Queue as q

class Queue(q):
	def __repr__(self):
		return f"Queue({self._qsize()})"

	def __add__(self, item):
		self.put(item)

	def __sub__(self, item):
		self.get()

qu = Queue()
qu + 9
qu + 7
qu - None
print(qu)
""" 
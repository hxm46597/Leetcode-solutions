from collections import  deque

from collections import deque


class Checkout:
	def __init__(self):
		self.queue = deque()
		self.deque = deque()

	def get_max(self):
		return self.deque[0] if self.deque else -1

	def add(self, value):
		self.queue.append(value)
		while self.deque and self.deque[-1] < value:
			self.deque.pop()
		self.deque.append(value)

	def remove(self):
		if not self.queue:
			return -1
		value = self.queue.popleft()
		if value == self.deque[0]:
			self.deque.popleft()
		return value

obj = Checkout()
#["Checkout","add","add","get_max","remove","get_max"]
print(obj.add(4))
print(obj.add(7))
print(obj.get_max())
print(obj.remove())
print(obj.get_max())
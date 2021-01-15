from collections import deque

class Stack:
	def __init__(self):
		self.container = deque()
	
	def push(self,val):
		self.container.append(val)
		
	def pop(self):
		return self.container.pop()
	
	def peek(self):
		return  self.container[-1]
	
	def is_empty(self):
		return len(self.container)==0
	
	def size(self):
		return len(self.container)

	def reverse_string(self, string):
	
		for ch in string:
			self.push(ch)

		rev = ''
		while self.size()!=0:
			rev += self.pop()

		return rev


if __name__ == '__main__':
	stack = Stack()
	print(stack.reverse_string("We will conquere COVID-19"))
	print(stack.reverse_string("91-DIVOC ereuqnoc lliw eW"))
	# should return "91-DIVOC ereuqnoc lliw eW"
class Stack:
	def __init__(self):
		# Initialise the stack's data attributes
		self.list = []
		pass
	
	def push(self, item):
		# Push an item to the stack
		self.list.append(item)
		pass

	def peek(self):
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty

		if len(self.list) ==0:
			return "Error"
		else:
			return self.list[-1]

	def pop(self):
		# Pop an item from the stack if non-empty
		if len(self.list) ==0:
			return " Error"
		else:
			self.list.pop()
			pass


	def is_empty(self):
		return len(self.list)==0

	def __str__(self):
		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
		s = ''
		for i in range(len(self.list)-1,-1,-1):
			s += str(self.list[i]) + ' '
			
			
		return s

	def __len__(self):
		# Return current number of elements in the stack
		return len(self.list)
		


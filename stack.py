import singlyLinkedList

# Implement stack with singly linked lists
class Stack:
	# constructor
	def __init__(self):
		stack = singlyLinkedList.SinglyLinkedList()
		self.stack = stack

	def push(self, data):
		self.stack.insertAtEnd(data)

	def pop(self):
		if self.stack.head == None:
			print("Stack is empty")
		else:
			self.stack.deleteFromEnd()

	def printStack(self):
		return self.stack.printList()

temp = Stack()
temp.push(5)
temp.push(6)
temp.push(7)
temp.push(8)
temp.pop()
temp.printStack() # [5, 6, 7]
temp.pop()
temp.pop()
temp.pop()
temp.pop() # list is already empty

# Node of a Singly Linked List
class Node:
	# constructor
	def __init__(self):
		self.data = None
		self.next = None

	# Method for setting the data field of the node
	def setData(self, data):
		self.data = data

	# Method for getting the data field of the node
	def getData(self):
		return self.data

	# Method for setting the next field of the node
	def setNext(self, next):
		self.next = next

	# Method for getting the next field of the node
	def getNext(self):
		return self.next

	# method for determining whether the node points
	# to another node
	def hasNext(self):
		return self.next != None

	# __str__ returns string equivalent of Object
	def __str__(self):
		return "Node[Data=%s]"%(self.data,)

class SinglyLinkedList:
	# constructor
	def __init__(self):
		self.head = None
		self.length = 0

	# Python is garbage-collected, so if you reduce the size
	# of your list, it will reclaim memory
	def clear(self):
		self.head = None
		self.length = 0

	# Method for getting the length (number of nodes)
	# of the linked list
	def listLength(self):
		counter = 0
		currNode = self.head
		while (currNode.getNext() != None):
			counter += 1
			currNode = currNode.getNext()
		return counter


	# Method for inserting a new node at the beginning
	# of the Linked List (at the head)
	def insertAtBeginning(self, data):
		newHead = Node()
		newHead.setData(data)

		if self.head == None:
			self.head = newHead
		else:
			currHead = self.head
			newHead.setNext(currHead)
			self.head = newHead

	# method to delete the first node of the linked list
	def deleteFromBeginning(self):
		if (self.length == 0):
			print("The list is empty")
		else:
			self.head = self.head.getNext()
			self.length -= 1

	# Method for inserting a new node at the end of the
	# Linked List
	def insertAtEnd(self, data):
		newTail = Node()
		newTail.setData(data)

		current = self.head
		while (current is not None and current.getNext() != None):
			current = current.getNext()

		if (current == None):
			self.head = self.tail = newTail
		else: 
			current.setNext(newTail)
		self.length += 1

	# Method to delete the last node of a linked list
	def deleteFromEnd(self):
		if (self.length == 0):
			print("The list is empty")
		else:
			current = self.head
			previous = self.head
			while (current.getNext() != None):
				previous = current
				current = current.getNext()
			previous.setNext(None)
			self.length -= 1


	# Method for inserting a new node at any position in
	# the linked list
	def insertAtPos(self, pos, data):
		# Assertion checking
		if (pos > self.length) or (pos < 0):
			return None

		else:
			if (pos == self.length):
				self.insertAtEnd(data)
			else:
				newNode = Node()
				newNode.setData(data)

				current = self.head
				counter = 0
				while (counter < pos - 1):
					counter += 1
					current = current.getNext()

				newNode.setNext(current.getNext())
				current.setNext(newNode)
				self.length += 1

	# Delete with node from linked list
	def deleteFromLinkedListWithNode(self, node):
		if self.length == 0:
			raise ValueError("List is empty")
		else:
			current = self.head
			previous = None
			found = False

			while not found:
				if current == node:
					found = True
				elif current is None:
					raise ValueError("Node not in Linked List")
				else:
					previous = current
					current = current.getNext()

		if previous is None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
		self.length -= 1

	# Delete with data from linked list
	def deleteValue(self, value):
		currentNode = self.head
		previousNode = self.head

		while currentNode.getNext() != None or currentNode.getData() != value:
			if currentNode.getData() == value:
				previousNode.setNext(currentNode.getNext())
				self.length -= 1
				return
			else:
				previousNode = currentNode
				currentNode = currentNode.getNext()
		print("The value provided is not present")

	# Method to delete a node at a particular position
	def deleteAtPosition(self,pos):
		counter = 0
		currentNode = self.head
		previousNode = self.head

		if pos > self.length or pos < 0:
			print("The position does not exist. Please enter a valid position.")
		else:
			while currentNode.getNext() != None or counter < pos:
				counter += 1
				if counter == pos:
					previousNode.setNext(currentNode.getNext())
					self.length -= 1
					return
				else:
					previousNode = currentNode
					currentNode = currentNode.getNext()

	def printList(self):

		currNode = self.head
		while currNode is not None:
			print(str(currNode))
			currNode = currNode.getNext()

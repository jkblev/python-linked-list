"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    current = head
    newNode = Node(data, next_node=None)

    # empty list
    if (current is None):
        return newNode

    while (current.next is not None):
        current = current.next
    current.next = newNode
    return head

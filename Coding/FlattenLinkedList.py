"""
http://blog.gainlo.co/index.php/2016/06/12/flatten-a-linked-list/

"""

class Node:
	def __init__(self, val):
		self.val = val
		self.next = self.child = None

def flattenLinkedList(head):
	stack = [head] # keeps track of level; I come back to a level only after finishing children from lower level.
	prev = None
	while stack:
		cur = stack.pop()
		if prev:
			prev.next = cur
		if cur.next:
			stack.append(cur.next)
		if cur.child:
			stack.append(cur.child)
		prev = cur
	return head





"""
Given two binary trees add them. Example:
   3          2          5
  / \    +   /     =    / \
 4   5      3          7   5
"""

class Node():
	def __init__(self, v):
		self.val = v
		self.left = None
		self.right = None



def addTrees(t1,t2):
	if t1 == None and t2 == None:
		return None
	elif t2 == None:
		return t1
	elif t1 == None:
		return t2
	t1.val += t2.val
	t1.left = addTrees(t1.left,t2.left)
	t1.right = addTrees(t1.right,t2.right)
	return t1



def preOrder(t):
	if t == None:
		print("_")
		return	
	print(t.val)
	preOrder(t.left)
	preOrder(t.right)



t1 = Node(1)
t1.left = Node(2)
t1.right = Node(3)
preOrder(t1)


t2 = Node(1)
t2.right = Node(3)
preOrder(t2)


preOrder(addTrees(t1,t1))
preOrder(addTrees(t2,t))



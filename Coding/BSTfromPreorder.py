"""
https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/
"""


class Node:
	def __init__(self, val):
		self.val = val
		self.left = self.right = None

class BST:

	def __init__(self, root):
		self.root = root

	def constructBST(self, preorder):
		self.idx = 0

		def helper(low, high):
			if self.idx >= len(preorder):
				return None
			val = preorder[self.idx]
			if val > high or val < low:
				return None
			node = Node(val)
			self.idx += 1
			node.left = helper(low, val)
			node.right = helper(val+1, high)
			return node

		self.root = helper(float('-inf'), float('inf'))
		return self.root

	def constructBSTitr(self, preorder):
		if not preorder:
			return None
		self.root = Node(None)
		stack = [(self.root, float('-inf'), float('inf'))]
		idx = 0
		while stack:
			node, low, high = stack.pop()
			
			if idx >= len(preorder):
				continue

			val = preorder[idx]
			if val < low or val > high:
				continue
			node.val = val
			idx += 1
			node.left = Node(None)
			node.right = Node(None)
			stack.append((node.right, val+1, high))
			stack.append((node.left, low, val))
			
		return self.root

	def preorder(self, node):
		if not node:
			return
		print(node.val)
		self.preorder(node.left)
		self.preorder(node.right)


bst = BST(None)
bst.constructBSTitr([10, 5, 1, 7, 40, 50])
bst.preorder(bst.root)


"""
https://massivealgorithms.blogspot.com/2019/02/sink-zeros-in-binary-tree.html
"""

class Node:
	def __init__(self, val):
		self.val = val
		self.left = self.right = None

class SinkZeros:
	def sinkZeros(self, root):
		self.stack = []
		self.zeros = 0
		def dfs(node):
			if not node:
				return
			if node.val == 0:
				self.zeros += 1
			else:
				self.stack.append(node.val)
			dfs(node.left)
			dfs(node.right)
			if self.zeros > 0:
				node.val = 0
				self.zeros -= 1
			else:
				node.val = self.stack.pop()
		dfs(root)
		return root

	def printTree(self, node):
		def helper(node):
			if not node:
				print('x', end=' ')
				return
			print(node.val, end=' ')
			helper(node.left)
			helper(node.right)
		print("------")
		helper(node)
		print()
		print("------")

	def testSk(self, node):
		self.printTree(node)
		self.sinkZeros(node)
		self.printTree(node)

	def test():
		root0 = Node(0)
		root0.left = Node(0)
		root0.left.left = Node(0)
		root0.right = Node(0)
		root0.right.left = Node(1)


		root1 = Node(0)

		root2 = Node(0)
		root2.left = Node(3)
		root2.left.left = Node(4)
		root2.right = Node(0)
		root2.right.left = Node(0)
		root2.right.left.right = Node(1)
		root2.right.right = Node(2)


		tests = [root0, root1, root2]
		sk = SinkZeros()
		for tt in tests:
			sk.testSk(tt)


SinkZeros.test()


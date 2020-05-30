"""
https://www.geeksforgeeks.org/check-if-leaf-traversal-of-two-binary-trees-is-same/
"""


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


# Solution 1
# O(N+M) space O(N+M) time
def binaryTreeLeaves(root1, root2):
	leaf1 = []
	leaf2 = []
	# The order in which we see leaves will
	# be maintained as it is inorder traversal.
	def dfs(node, leafs):
		if not node:
			return
		if not node.left and not node.right:
			leafs.append(node)
			return
		dfs(node.left, leafs)
		dfs(node.right, leafs)
	dfs(root1, leaf1)
	dfs(root2, leaf2)
	return leaf1 == leaf2

print(binaryTreeLeaves(root, root1))


# O(h1+h2) space
def binaryTreeLeaves2(root1, root2):
	def isLeaf(node):
		return not node or node.left == node.right == None
	if not root1 and not root2:
		return True
	if (not root1) ^ (not root2):
		return False
	stack1 = [root1]
	stack2 = [root2]
	while stack1 or stack2:
		if (not stack1) ^ (not stack2):
			return False
		tmp1 = stack1.pop()
		while not isLeaf(tmp1):
			if tmp1.right:
				stack1.append(tmp1.right)
			if tmp1.left:
				stack1.append(tmp1.left)
			tmp1 = stack1.pop()
		tmp2 = stack2.pop()
		while not isLeaf(tmp2):
			if tmp2.right:
				stack2.append(tmp2.right)
			if tmp2.left:
				stack2.append(tmp2.left)
			tmp2 = stack2.pop()
		if ((not tmp1) ^ (not tmp2)) or (tmp1 and tmp2 and tmp1.val != tmp2.val):
			return False		
	return True


## TEST 1: True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(6) 
root.right.right = Node(7)

root1 = Node(0)
root1.left = Node(5)
root1.right = Node(8)
root1.left.right = Node(4)
root1.right.left = Node(6)
root1.right.right = Node(7)

print(binaryTreeLeaves2(root, root1))

## TEST 1: False

root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(8)
root.left.right = Node(9)

root1 = Node(1)
root1.left = Node(4)
root1.right = Node(3)
root1.left.right = Node(8)
root1.right.left = Node(2)
root1.right.right = Node(9)

print(binaryTreeLeaves2(root, root1))






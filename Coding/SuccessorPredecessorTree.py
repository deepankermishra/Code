class Node:
	def __init__(self, val):
		self.val = val
		self.left = self.right = None

def traverseTogether(root):
	left = []
	right = []
	def goLeft(node):
		while node:
			left.append(node)
			node = node.left
	def goRight(node):
		while node:
			right.append(node)
			node = node.right
	goLeft(root)
	goRight(root)
	while left and right:
		lp = left.pop()
		rp = right.pop()
		if lp == rp:
			print(lp.val)
			break
		print(lp.val, rp.val)
		goLeft(lp.right)
		goRight(rp.left)
		if lp == right[-1] or rp == left[-1]:
			break

root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
# root.right.right = Node(8)

traverseTogether(root)


def countNodes(root, idx):
	if not root:
		return idx
	l = countNodes(root.left, idx)
	print(root.val, l+1)
	return countNodes(root.right, l+1)


countNodes(root,0)


def findKthLargest(root, k):
	ans = []
	idx = [0]
	def dfs(node, k):
		if not node or ans:
			return
		dfs(node.left, k)
		idx[0] += 1
		if idx[0] == k:
			ans.append(node.val)
		dfs(node.right, k)
	dfs(root, k)
	return ans[0] if ans else -1

print(findKthLargest(root,2))


def LCA(r,p,q):
	def leastCommonAncestor(root, p, q):
		if not root:
			return (None, 0)
		left = leastCommonAncestor(root.left, p, q)
		if left[1] == 2:
			return left
		right = leastCommonAncestor(root.right, p, q)
		if right[1] == 2:
			return right
		if ((left[1] and right[1]) or
		 (root == p and (left[0] == q or right[0] == q)) or
		  (root == q and (left[0] == p or right[0] == p))):
			return (root,2)
		if root in [p, q]:
			return [root, 1]
		return [None, 0]
	lca, votes = leastCommonAncestor(r,p,q)
	return lca.val if votes == 2 else None

print(LCA(root,root.left.right, Node(10)))

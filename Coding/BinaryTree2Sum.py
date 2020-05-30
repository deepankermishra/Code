"""
Given a binary tree and an integer K, return two nodes which are at different level and their sum is equal to K.

Constraints :

Tree can have duplicate values.
Incase more than one pair is available in the tree, then return any of the pair.
"""


def sumNodes(node, K, level, lookup):
	if not node:
		return

	if (K - node.val) in lookup:
		for n,l in lookup[K-node.val]:
			if l != level:
				return (node, n)

	lookup[node.val].append((node,level))

	res = sumNodes(node.left, K, level+1, lookup)
	if res:
		return res
	return sumNodes(node.right, K, level+1, lookup)



"""
Given a binary tree containing n distinct numbers and a value x.
The problem is to count pairs in the given binary tree whose sum is equal to the given value x.
1. use the above function and count pairs

"""


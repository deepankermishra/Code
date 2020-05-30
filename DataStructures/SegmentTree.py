"""
https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
1. It's a full binary tree (0 or 2 children), unlike heap which is a complete binary tree.
2. Thus last node can have empty elements in an array representation.

Here we are generating segment tree for range sum queries.
"""

def segmentTree(arr):
	n = len(arr)
	tree = [0] * MAX_SIZE 

	def helper(arr, l, h, idx, tree):
		if l == h:
			tree[idx] = arr[l]
			return arr[l]
		m = l + (h-l)//2
		left = helper(arr, l, m, idx*2+1, tree)
		right = helper(arr, m+1, h, idx*2+2, tree)
		tree[idx] = left + right

	helper(arr,0,len(arr)-1,0,tree)
	return tree

def getResult(st, idx, ss, se, qs, qe):
	if qe < ss or sq < qs:
		return 0
	if ss >= qs and se <= qe:
		return st[idx]
	m = (se-ss)//2 + ss
	return getResult(st, idx*2+1, ss, m, qs, qe) + getResult(st, idx*2+2, m+1, se, qs, qe)


def updateValue(st, idx, ss, se, at, diff):
	if at < ss or at > se:
		return
	st[idx] += diff
	if (ss != se):
		m = ss + (se-ss)//2
		updateValue(st, idx*2+1, ss, m, at, diff)
		updateValue(st, idx*2+2, m+1, se, at, diff)


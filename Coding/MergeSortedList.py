class Node:
	def __init__(self, v):
		self.val = v
		self.next = None

class List:
	def __init__(self):
		self.head = self.tail = None
		self.size = 0

	def add(self, val):
		if self.tail:
			self.tail.next = Node(val)
		else:
			self.tail = self.head = Node(val)
		self.tail = self.tail.next
		self.size += 1


def mergeSortedList(l1, l2):
	cur1, cur2 = l1, l2
	cur = None
	head = None
	while cur1 and cur2:
		if cur1.val < cur2.val:
			if cur:
				cur.next = cur1
				cur = cur1
			else:
				cur = cur1
				head = cur
		else:
			if cur:
				cur.next = cur2
				cur = cur2
			else:
				cur = cur2
				head = cur
	if cur1:
		cur.next = cur1
	elif cur2:
		cur.next = cur2
	else:
		cur.next = None
	return head






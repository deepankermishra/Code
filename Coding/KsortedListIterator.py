import heapq # gives a min heap
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

# Space = O(K) Time = O(KlogK + NlogK)
class KSortedListIterator:
	def __init__(self, kLinkNodes):
		self.heap = []
		self.kLinkNodes = kLinkNodes
		self.K = len(kLinkNodes)

	def iter(self):
		# kLinkNodes has the head of all k linked lists
		if self.heap:
			val, idx = heapq.heappop(self.heap) #O(logk)
			node = self.kLinkNodes[idx]
			if node and node.next:
				heapq.heappush(self.heap, (node.next.val, idx)) #O(logk)
			if node:
				self.kLinkNodes[idx] = self.kLinkNodes[idx].next
			return node
		else:
			# start or end
			for ii in range(self.K): #O(klogk)
				node = self.kLinkNodes[ii]
				if node:
					heapq.heappush(self.heap, (node.val, ii))
			if not self.heap: # end of iteration
				return None
			return self.iter()

	def test():
		l0 = Node(0)
		l0.next = Node(1)
		l0.next.next = Node(2)
		l0.next.next.next = Node(2)

		l1 = Node(0)
		l1.next = Node(1)
		l1.next.next = Node(5)
		l1.next.next.next = Node(6)

		l2 = Node(0)
		l2.next = Node(1)
		l2.next.next = Node(3)
		l2.next.next.next = Node(4)


		it = KSortedListIterator([l0,l1,l2])
		while 1:
			n = it.iter()
			if not n:
				break
			print(n.val, end = ' ')

		print()


KSortedListIterator.test()







class Node():
	def __init__(self, v):
		self.val = v
		self.next = None

class List():
	def __init__(self):
		self.head = None

	def length(self):
		c = 0
		n = self.head
		while n:
			c+=1
			n = n.next
		return c

	def push(self,v):
		if self.head == None:
			self.head = Node(v)
		else:
			cur, nex = self.head, self.head.next
			while nex:
				cur = nex
				nex = nex.next
			cur.next = Node(v)
	def dedup(self):
		if self.head == None:
			return
		seen = {}
		pre, cur = None, self.head
		while cur:
			if cur.val in seen:
				# delete cur
				pre.next = cur.next
				del cur
				cur = pre.next
			else:
				seen[cur.val] = 1
				pre = cur
				cur = cur.next
	def printMe(self):
		cur = self.head
		if cur:
			print(cur.val, end="")
			cur = cur.next
		while cur:
			print("->", end="")
			print(cur.val, end="")
			cur = cur.next
		print("")

def sumList(l1,l2,c,sl):
	if l1 == None and l2 == None and c == 0:
		return
	l1v = l1.val if l1 else 0
	l2v = l2.val if l2 else 0
	curSum = l1v + l2v + c
	c = 1 if curSum >= 10 else 0
	sl.push(curSum%10)
	l1n = l1.next if l1 else None
	l2n = l2.next if l2 else None
	sumList(l1n,l2n,c,sl)

# 1>2>3
# 1>2>3>4
# 1

def middleElement(l):
	p1, p2 = l.head, l.head
	while p2:
		if p2.next:
			p2 = p2.next.next
		else:
			return p1
		p1 = p1.next
	return p1

def match(s,e):
	if (s.next == e.next or (s.next == e and e.next == s)):
		return True
	return s.val == e.val and match(s.next,e.next)

# c -> n -> nn
def reverse(s):
	c,n = s, s.next
	while n:
		tmp, n.next = n.next, c
		c, n = n, tmp
	s.next = None
	return c

def isPalindrome(l):
	m = middleElement(l)
	s = l.head
	if m == s:
		return True
	elif s.next == m and m.next == None:
		if s.val == m.val:
			return True
		else:
			return False
	e = reverse(m)
	ans = match(s,e)
	reverse(e)
	return ans

sl = List()
sl.push(3)
sl.push(1)
sl.push(3)
print(isPalindrome(sl))



l1 = List()
l1.push(7)
l1.push(1)
l1.push(6)
l2 = List()
l2.push(5)
l2.push(9)
l2.push(2)
ansl = List()
sumList(l1.head,l2.head,0,ansl)
ansl.printMe()

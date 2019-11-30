"""
You are given an integer N. You have to find smallest multiple of N which consists of digits 0 and 1 only. Since this multiple could be large, return it in form of a string.
Note : returned string should not contain any leading zeroes.
"""

def multipleOfN(n):
	visited = {}
	stack = ["1"]
	while len(stack):
		s = stack.pop()
		r = int(s) % n
		if r == 0:
			return s
		visited[r] = 1
		t = s + "0"
		if int(t) % n not in visited:
			stack.append(t)
		t = s + "1"
		if int(t) % n not in visited:
			stack.append(t)


for i in range(1,10):
	print(multipleOfN(i))
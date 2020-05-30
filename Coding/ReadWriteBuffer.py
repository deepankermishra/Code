class ReadWriteBuffer:
	def __init__(self, size):
		self.buf = ['']*(size+1)
		self.l = self.r = 0
		self.sz = size+1
	def read(self, chars, n):
		cnt = 0
		while cnt < n and self.l != self.r:
			self.l = (self.l+1) % self.sz
			chars[cnt] = self.buf[self.l]
			cnt += 1
		return cnt
	def write(self, chars):
		cnt = 0
		while cnt < len(chars) and (self.r+1)%self.sz != self.l:
			self.r = (self.r+1) % self.sz
			self.buf[self.r] = chars[cnt]
			cnt += 1
		return cnt



rwbuf = ReadWriteBuffer(5)
rwbuf.write('abcdef')
print(rwbuf.buf)
n = 1
chars = [None] * n
rwbuf.read(chars,n)
print(chars)
rwbuf.write('abcdef')
print(rwbuf.buf)
n = 2
chars = [None] * n
rwbuf.read(chars,n)
print(chars)
rwbuf.write('abcdef')
print(rwbuf.buf)
n = 3
chars = [None] * n
rwbuf.read(chars,n)
print(chars)



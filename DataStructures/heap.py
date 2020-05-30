# Enter your code here. Read input from STDIN. Print output to STDOUT

class Heap():
    def __init__(self):
        self.a = []
        self.s = 0
    
    def push(self, v):
        if self.s < len(self.a):
            self.a[self.s] = v
        else:
            self.a.append(v)
        self.heapup(self.s)
        self.s += 1
    
    def delete(self, v):
        at = 0
        while self.a[at] != v:
            at += 1
        self.s -= 1
        self.a[at], self.a[self.s] = self.a[self.s], self.a[at]
        self.heapdown(at)

    def pop(self):
        top = self.a[0]
        self.a[0] = self.a[self.s-1]
        self.heapdown(0)
        self.s -= 1
        return top

    def top(self):
        return self.a[0]
    
    def heapup(self, at):
        if at <= 0:
            return
        if at & 1:
            p = (at-1) >> 1
        else:
            p = (at-2) >> 1
        if self.a[p] > self.a[at]:
            self.a[at], self.a[p] = self.a[p], self.a[at]
            self.heapup(p)
    
    def heapdown(self, at):
        if at >= self.s:
            return
        l, r = at*2 + 1, at*2 + 2
        if l >= self.s:
            return
        if self.a[l] < self.a[at]:
            if r >= self.s:
                self.a[l], self.a[at] = self.a[at], self.a[l]
                self.heapdown(l)
            elif self.a[r] < self.a[l]:
                self.a[r], self.a[at] = self.a[at], self.a[r]
                self.heapdown(r)
            
        
heap = Heap()
q = int(input())
while q:
    cmd = list(map(int, input().split()))
    print("cmd: ", cmd)
    if cmd[0] == 1:
        heap.push(cmd[1])
    elif cmd[0] == 2:
        heap.delete(cmd[1])
    else:
        print(heap.top())
    print("heap: ", heap.a[:heap.s])
    q -= 1

def heapdown(arr, s):
	if s >= len(arr):
		return
	l, r = 2*s+1, 2*s+2
	if l < len(arr) and arr[l] < arr[s]:
		if r < len(arr) and arr[r] < arr[l]:
			arr[r], arr[s] = arr[s] , arr[r]
			heapdown(arr,r)
		else:
			arr[l], arr[s] = arr[s], arr[l]
			heapdown(arr, l)
	if r < len(arr) and arr[r] < arr[s]:
		arr[r], arr[s] = arr[s] , arr[r]
		heapdown(arr,r)

def heapify(arr):
	n = len(arr)
	s = n>>1
	for at in range(s-1, -1,-1):
		heapdown(arr,at)

def popMin(arr):
	ans = arr[0]
	arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]
	del arr[len(arr)-1]
	heapdown(arr,0)
	return ans

arr = [3,2,1,4,5,6,0,7]
heapify(arr)
print(arr)
popMin(arr)
print(arr)
popMin(arr)
print(arr)
popMin(arr)
print(arr)

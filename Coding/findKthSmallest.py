def kthSmallest(arr, k):
	# using quick select
	k -= 1

	def partition(arr, l, h):
		if l == h:
			return l
		pivot = arr[h]
		idx = l
		for i in range(l, h):
			if arr[i] < pivot:
				arr[idx], arr[i] = arr[i], arr[idx]
				idx += 1
		arr[idx], arr[h] = arr[h], arr[idx]
		return idx
	
	if k < 0 or k > len(arr):
		return None

	l, h = 0, len(arr) - 1
	while l <= h:
		p = partition(arr, l, h)
		if p == k:
			return arr[p]
		elif p > k:
			h = p - 1
		else:
			l = p + 1


print(kthSmallest([9,3,5,2,34,1],2))
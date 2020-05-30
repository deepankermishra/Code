"""https://leetcode.com/discuss/interview-question/537699/"""

"""
Memoized solution.
This may waste space as we only need values from i+2 to i+6
"""
def optimalGame(arr):
	# Helper returns the maximum sum of cards for remaining arr for
	# player 1.
	def helper(arr, i, cache):
		if i in cache:
			return cache[i]
		if i >= len(arr):
			return 0
		pick1 = arr[i]+ min(helper(arr, i+2, cache), helper(arr, i+3, cache), helper(arr,i+4, cache))
		pick2 = 0
		if i+1 < len(arr):
			pick2 = arr[i]+arr[i+1]+ min(helper(arr, i+3, cache), helper(arr, i+4, cache), helper(arr,i+5, cache))
		pick3 = 0
		if i+2 < len(arr):
			pick3 = arr[i]+arr[i+1]+arr[i+2] + min(helper(arr, i+4, cache), helper(arr, i+5, cache), helper(arr,i+6, cache))
		cache[i] = max(pick1, pick2, pick3)
		return cache[i]
	return helper(arr, 0, {})

print(optimalGame([1,2,-3,8]))
print(optimalGame([1, 1, 1, 1, 100]))


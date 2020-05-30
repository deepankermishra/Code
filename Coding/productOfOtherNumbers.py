"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution!

https://www.interviewcake.com/question/python/product-of-other-numbers
"""


def productExceptSelf(arr):
	n = len(arr)
	prod = [1] * n
	cur = 1
	for i in range(1,n):
		cur = cur * arr[i-1]
		prod[i] = cur
	cur = 1
	for i in range(n-2,-1,-1):
		cur = cur * arr[i+1]
		prod[i] *= cur
	return prod

print(productExceptSelf([1,7,3,4]))
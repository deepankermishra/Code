"""
Find the longest path in a matrix with given constraints
Given a n*n matrix where all numbers are distinct, find the maximum
length path (starting from any cell) such that all cells along the 
path are in increasing order.

We can move in 4 directions from a given cell (i, j), i.e., we can
move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1).

Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9. 
"""

def maxLenPath(M):
	visited = {}
	maxLenPathVal = [float("-inf")]

	def maxLenPathHelp(M,n,m,i,j):
		if (i,j) in visited:
			return visited[(i,j)]
		visited[(i,j)] = 0
		pathLen = 1		
		if i+1 < n and M[i+1][j] > M[i][j]:
			pathLen = max(pathLen,1+maxLenPathHelp(M,n,m,i+1,j))
		if j+1 < m and M[i][j+1] > M[i][j]:
			pathLen = max(pathLen,1+maxLenPathHelp(M,n,m,i,j+1))
		if i-1 >= 0 and M[i-1][j] > M[i][j]:
			pathLen = max(pathLen,1+maxLenPathHelp(M,n,m,i-1,j))
		if j-1 >= 0 and M[i][j-1] > M[i][j]:
			pathLen = max(pathLen,1+maxLenPathHelp(M,n,m,i,j-1))
		visited[(i,j)] = max(pathLen,visited[(i,j)])
		maxLenPathVal[0] = max(maxLenPathVal[0],visited[(i,j)])
		return visited[(i,j)]

	maxLenPathHelp(M,len(M),len(M[0]),0,0)
	
	return maxLenPathVal[0]


m = [[2,3,4],[2,1,5],[4,5,6],[9,8,7]]

maxLenPath(m)


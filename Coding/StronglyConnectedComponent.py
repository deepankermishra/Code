"""
SCC in directed graph.

Each vertex is represented using 0 to n-1.

List of vertices.
Adjacency list of edges.

Return representative of each component.

If we replace SCCs by their representatives in a directed graph we will get a DAG.
"""

def kasarajuAlgorithm(vertices, edges):
	n = len(vertices)
	visited = [0]*n
	finishStack = []

	def dfs(node):
		visited[node] = 1
		for ngh in edges[node]:
			if not visited[ngh]:
				dfs(ngh)
		finishStack.append(node)

	for node in range(n):
		if not visited[node]:
			dfs(node)

	visitRev = [0]*n
	who = [0]*n
	reverseEdges = [[] for _ in range(n)]
	
	for node in range(n):
		for ngh in edges[node]:
			reverseEdges[ngh].append(node)

	def dfsRep(node, rep):
		visitRev[node] = 1
		who[node] = rep
		for ngh in reverseEdges[node]:
			if not visitedRev[ngh]:
				dfsRep(ngh, rep)


	while finishStack:
		st = finishStack.pop()
		dfsRep(st, st)

	return who

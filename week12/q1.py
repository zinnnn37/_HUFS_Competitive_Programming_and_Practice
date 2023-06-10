from copy import deepcopy
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

def _topology_sort(i):
	res = []
	q = deque()
	q.append(i)
	copied = deepcopy(indegree)

	while q:
		print(q)
		cur = q.popleft()
		res.append(cur)

		for i in island[cur]:
			copied[i] -= 1
		
			if copied[i] == 0:
				q.append(i)
	
	return len(res)

def topology_sort(m, n):
	reslen = 0

	for i in range(n):
		if indegree[i] == 0:
			reslen = max(reslen, _topology_sort(i))

	print(reslen)

if __name__ == "__main__":
	m, n = map(int, input().split())
	island = [[] for _ in range(n)]
	indegree = [0] * (n)
	for _ in range(m):
		a, b = map(int, input().split())
		island[a].append(b)
		indegree[b] += 1
			
	print(indegree)

	topology_sort(m, n)
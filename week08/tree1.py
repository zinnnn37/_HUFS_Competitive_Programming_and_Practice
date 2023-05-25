from collections import deque
import sys
sys.setrecursionlimit(10**8)
input = lambda: sys.stdin.readline().rstrip()

def _dfs(q, visited):
	while q:
		cur = q.popleft()
		pre.append(cur)
		for child in tree[cur]:
			q.append(child)
			_dfs(q, visited)
		post.append(cur)

def dfs():
	visited = [False] * (n + 1)
	q = deque()
	q.append(1)
	_dfs(q, visited)

def query_ancestor(a, b):
	if pre.index(a) > pre.index(b):
		return False
	if post.index(a) < post.index(b):
		return False
	return True

if __name__ == "__main__":
	n, q = map(int, input().split())
	tree = [[] for _ in range(n + 1)]

	for _ in range(n-1):
		a, b = map(int, input().split())
		tree[a].append(b)

	pre, post = [], []
	dfs()

	cnt = 0
	for _ in range(q):
		a, b = map(int, input().split())
		if (query_ancestor(a, b)):
			cnt += 1
	print(cnt)

'''
수행시간:
	dfs() 함수에서 자식 노드를 한 번씩 방문하므로 O(n)시간이 소요되고
	query_ancestor() 함수에서 index() 함수를 사용하므로 O(n)시간이 소요된다.
	따라서 총 수행시간은 O(2n) = O(n)이다.
'''
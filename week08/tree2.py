from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**8)

def _postorder(q, visited, parent):
	while q:
		cur = q.popleft()
		for child in tree[cur]:
			q.append(child)
			_postorder(q, visited, cur)
		if not visited[cur]:
			parents[cur] = parent
			w[parent] += w[cur]
			visited[cur] = True

def postorder():
	visited = [False] * (n + 1)
	q = deque()
	q.append(1)
	_postorder(q, visited, 0)

def _update(q, diff):
	while q:
		cur = q.popleft()
		if parents[cur] != 0:
			q.append(parents[cur])
			w[parents[cur]] += diff
			_update(q, diff)

def update(v, diff):
	q = deque()
	q.append(v)
	w[v] += diff
	_update(q, diff)

if __name__ == '__main__':
	n, q = map(int, input().split())
	tree = [[] for _ in range(n + 1)]
	w = [0] + list(map(int, input().split()))

	for _ in range(n-1):
		p, c = map(int, input().split())
		tree[p].append(c)

	parents = [0] * (n + 1)
	postorder()

	for _ in range(q):
		cmd, *v = input().split()
		v = list(map(int, v))
		if cmd == 'subtree':
			print(w[v[0]])
		if cmd == 'update':
			update(v[0], v[1])
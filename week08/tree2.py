from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

def update()

def _preorder(q, visited, parent):
	while q:
		cur = q.popleft()
		if not visited[cur]:
			pre.append(cur)
			visited[cur] = True
			cost[cur] += w[cur]
		for child in tree[cur]:
			q.append(child)
			subtree[cur] += 1
			_preorder(q, visited, cur)
		subtree[parent] += subtree[cur]
		cost[parent] += cost[cur]

def preorder():
	visited = [False] * (n + 1)
	q = deque()
	q.append(1)
	_preorder(q, visited, 1)
	subtree[1] //= 2
	cost[1] //= 2

if __name__ == '__main__':
	n, q = map(int, input().split())
	tree = [[] for _ in range(n + 1)]
	w = [0] + list(map(int, input().split()))

	for _ in range(n-1):
		p, c = map(int, input().split())
		tree[p].append(c)

	pre = []
	cost = [0] * (n+1)
	subtree = [0] * (n+1)
	preorder()
	print(pre)
	print(subtree)
	print(cost)

	for _ in range(q):
		cmd, *v = input().split()
		v = list(map(int, v))
		if cmd == 'subtree':
			print(cost[v[0]])
		#if cmd == 'update':
		#	update(v[0], v[1])
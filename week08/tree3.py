from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**8)

def _sum(q, res):
	while q:
		cur = q.popleft()
		for parent in rev[cur]:
			q.append(parent)
			res += w[parent]
			res = _sum(q, res)
	return res

def sum(v):
	q = deque()
	q.append(v)
	res = w[v]
	print(_sum(q, res))

def update(v, diff):
	q = deque()
	q.append(v)
	w[v] += diff

if __name__ == '__main__':
	n, q = map(int, input().split())
	tree = [[] for _ in range(n + 1)]
	rev = [[] for _ in range(n + 1)]
	w = [0] + list(map(int, input().split()))

	for _ in range(n-1):
		p, c = map(int, input().split())
		tree[p].append(c)
		rev[c].append(p)

	for _ in range(q):
		cmd, *v = input().split()
		v = list(map(int, v))
		if cmd == 'sum':
			sum(v[0])
		if cmd == 'update':
			update(v[0], v[1])
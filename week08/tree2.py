from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

def init(node, s, e):
	if s == e:
		bit[node] = tree[s]
		return bit[node]
	mid = (s + e) // 2
	bit[node] = init(node * 2, s, mid) + init(node * 2 + 1, mid + 1, e)
	return bit[node]

def update(node, s, e, idx, diff):
	if idx < s or idx > e:
		return
	bit[node] += diff
	if s != e:
		mid = (s + e) // 2
		update(node * 2, s, mid, idx, diff)
		update(node * 2 + 1, mid + 1, e, idx, diff)

def query_subtree(v):
	pass

def query_update(v, w):
	pass

if __name__ == "__main__":
	n, q = map(int, input().split())
	tree = [[] for _ in range(n + 1)]
	bit = [0] * (n * 4)

	w = list(map(int, input().split()))

	for _ in range(n-1):
		a, b = map(int, input().split())
		tree[a].append(b)

	for _ in range(q):
		cmd, *v = input().split()
		v = list(map(int, v))
		if cmd == 'subtree':
			query_subtree(v[0])
		elif cmd == 'update':
			query_update(v[0], v[1])

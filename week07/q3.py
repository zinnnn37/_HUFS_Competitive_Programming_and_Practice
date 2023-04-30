import sys
input = lambda: sys.stdin.readline().rstrip()

def update(tree, idx, diff, node, start, end):
	if not (start <= idx <= end):
		return
	tree[node] += diff
	if start == end:
		return
	mid = (start + end) // 2
	update(tree, idx, diff, node * 2, start, mid)
	update(tree, idx, diff, node * 2 + 1, mid + 1, end)

def query(tree, qstart, qend, node, start, end):
	if qstart <= start and end <= qend:
		return tree[node]
	if qend < start or end < qstart:
		return 0
	mid = (start + end) // 2
	return query(tree, qstart, qend, node * 2, start, mid) + query(tree, qstart, qend, node * 2 + 1, mid + 1, end)

if __name__ == '__main__':
	n = int(input())
	a1 = list(map(int, input().split()))
	a2 = list(map(int, input().split()))

	a1, a2 = zip(*sorted(zip(a1, a2)))

	t1 = [0] * (n * 4)
	t2 = [0] * (n * 4)

	ans = 0

	for i in range(n):
		s, e = i, i
		while (e < n - 1) and (a1[e] == a1[e+1]):
			e += 1
		for j in range(s, e):
			update(t2, a1[j], -1, 1, 0, n)
		for j in range(s, e):
			ans += query(t1, 0, a1[j], 1, 0, n) * query(t2, 0, a2[j], 1, 0, n)
		for j in range(s, e+1):
			update(t1, a2[j], 1, 1, 0, n)
		i = e
	print(ans)


'''

'''
import sys
input = lambda: sys.stdin.readline().rstrip()

def query_ancestor(a, b):
	if a == b:
		return True
	if a in tree[b]:
		return True
	for parent in tree[b]:
		if query_ancestor(a, parent):
			return True
	return False

if __name__ == "__main__":
	n, q = map(int, input().split())
	tree = [[] for _ in range(n + 1)]
	for _ in range(n-1):
		a, b = map(int, input().split())
		tree[b].append(a)
	
	cnt = 0
	for _ in range(q):
		a, b = map(int, input().split())
		if (query_ancestor(a, b)):
			cnt += 1
	print(cnt)
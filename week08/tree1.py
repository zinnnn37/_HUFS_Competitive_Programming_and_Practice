from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

def _preorder(q, visited):
	while q:
		cur = q.popleft()
		if not visited[cur]:
			pre.append(cur)
			visited[cur] = True
		for child in tree[cur]:
			q.append(child)
			_preorder(q, visited)

def preorder():
	visited = [False] * (n + 1)
	q = deque()
	q.append(1)
	_preorder(q, visited)

def _postorder(q, visited):
	while q:
		cur = q.popleft()
		for child in tree[cur]:
			q.append(child)
			_postorder(q, visited)
		if not visited[cur]:
			post.append(cur)
			visited[cur] = True

def postorder():
	visited = [False] * (n + 1)
	q = deque()
	q.append(1)
	_postorder(q, visited)

def query_ancestor(a, b):
	if pre.index(a) > pre.index(b):
		return False
	if post.index(a) < post.index(b):
		return False
	return True

if __name__ == "__main__":
	n, q = map(int, input().split())
	tree = [[] for _ in range(n + 1)]
	# 샹.. 결국에는 트리를 만들어야 한다

	for _ in range(n-1):
		a, b = map(int, input().split())
		tree[a].append(b)

	pre, post = [], []
	preorder()
	postorder()

	cnt = 0
	for _ in range(q):
		a, b = map(int, input().split())
		if (query_ancestor(a, b)):
			cnt += 1
	print(cnt)
from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**8)

def _sum(q, res):
	while q:
		cur = q.popleft()
		for parent in parents[cur]:
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
	parents = [[] for _ in range(n + 1)]
	w = [0] + list(map(int, input().split()))

	for _ in range(n-1):
		p, c = map(int, input().split())
		parents[c].append(p)

	for _ in range(q):
		cmd, *v = input().split()
		v = list(map(int, v))
		if cmd == 'sum':
			sum(v[0])
		if cmd == 'update':
			update(v[0], v[1])

'''
수행시간:
	sum() 함수에서 부모 노드를 한 번씩 방문하므로 최악의 경우 O(n)시간이 소요되고
	update() 함수에서 인덱스를 통해 가중치 배열을 업데이트하므로 O(1)시간이 소요된다.
	따라서 총 수행시간은 O(n)이다.
'''
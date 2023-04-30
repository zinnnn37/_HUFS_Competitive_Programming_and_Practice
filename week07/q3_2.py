import math
import sys
input = lambda: sys.stdin.readline().rstrip()

def get_sum(tree, idx):
	res = 0

	while idx > 0:
		sum += tree[idx]
		idx -= (idx & -idx)
		# 1이 존재하는 최하위 비트 찾기
		# 이를 빼면 누적합 인덱스를 얻을 수 있다
	return res

def update(tree, idx, diff):
	while idx < len(tree):
		tree[idx] += diff
		idx += (idx & -idx)

if __name__ == '__main__':
	n = int(input())
	p = list(map(int, input().split()))
	q = list(map(int, input().split()))
	
	p, q = zip(*sorted(zip(p, q)))
import sys
input = lambda: sys.stdin.readline().rstrip()

def tiling():
	pass

if __name__ == '__main__':
	n, k = map(int, input().split())
	matrix = [list(map(int, input().split())) for _ in range(n)]

	if n < k:
		print(-1)
	else:
		tiling()
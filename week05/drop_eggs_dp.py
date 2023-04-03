import sys
input = lambda: sys.stdin.readline().rstrip()

def init():
	for i in range(E+1):
		DP[E][1] = 1
		DP[E][0] = 0
	for j in range(F+1):
		DP[1][j] = j

def dp():
	for i in range(2, E+1):
		for j in range(2, F+1):
			DP[i][j] = sys.maxsize
			for k in range(1, j+1):
				cur = max(DP[i-1][k-1], DP[i][j-k]) + 1
				if cur < DP[i][j]:
					DP[i][j] = cur
	return DP[E][F]

if __name__ == '__main__':
	E, F = map(int, input().split())
	DP = [[0] * (F+1) for _ in range(E+1)]
	init()
	print(dp())
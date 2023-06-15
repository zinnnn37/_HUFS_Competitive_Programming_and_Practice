import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	n, k = map(int, input().split())
	A = list(map(int, input().split()))
	B = []

	for i in range(n - k + 1):
		window = A[i:i+k]
		min_value = min(window)
		B.append(min_value)

	print(*B)

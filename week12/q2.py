import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	n = int(input())
	f = list(map(int, input().split()))
	MAX = 14

	dp = [[0] * (n+1) for _ in range(MAX)]
	dp[0] = [0] + f

	for i in range(1, MAX):
		for j in range(n+1):
			dp[i][j] = dp[i-1][dp[i-1][j]]
	
	for _ in range(int(input())):
		x, k = map(int, input().split())

		for i in range(MAX):
			if k & (1 << i):
				x = dp[i][x]
	
		print(x)
	print(dp)

'''
알고리즘:
	n을 이진수로 바꾸어 조금 더 빠르게 계산할 수 있다.
	예를 들어, 13을 2진수로 바꾸면 1101이다.
	즉, 8(2^3) + 4(2^2) + 1(2^0) 이므로
	8회 계산한 값을 4회 계산한 값에 1회 계산한 값을 넣으면 된다.
	
	10,000은 이진수로 변환 시 비트가 14개이므로 MAX를 14로 설정한다.
	dp[i][j]는 j를 i레벨에서 계산한 값을 저장한다.

'''
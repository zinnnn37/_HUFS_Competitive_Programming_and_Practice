import sys
input = lambda: sys.stdin.readline().rstrip()

def LPS(s):
	n = len(s)

	if n == 1:
		return 1

	dp = [[0] * n for _ in range(n)]
	for i in range(n):
		dp[i][i] = 1	# 문자가 하나인 부분 수열

	for i in range(n-1):
		if s[i] == s[i+1]:
			dp[i][i+1] = 2

	for k in range(2, n+1):
		for i in range(n-k+1):
			j = i + k-1
			if s[i] == s[j]:
				dp[i][j] = dp[i+1][j-1] + 2
			else:
				dp[i][j] = max(dp[i][j-1], dp[i+1][j])

	return dp[0][n-1]

if __name__ == '__main__':
	s = input()

	print(LPS(s))
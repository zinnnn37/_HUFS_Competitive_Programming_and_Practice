import sys
input = lambda: sys.stdin.readline().rstrip()

def almost_palindrome():
	if s == s[::-1]:
		return 0;

	for j in range(1, n):
		for i in range(j-1, -1, -1):
			if i == j-1:
				if s[i] != s[j]:
					dp[i][j] = 1
			else:
				if s[i] == s[j]:
					dp[i][j] = dp[i+1][j-1]
				else:
					dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
	
	return dp[0][-1] if dp[0][-1] <= 3 else -1

if __name__ == '__main__':
	s = input()
	n = len(s)
	dp = [[0] * n for _ in range(n)]
	print(almost_palindrome())
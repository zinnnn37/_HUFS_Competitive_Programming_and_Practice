import sys
input = lambda: sys.stdin.readline().rstrip()

def almost_palindrome():
	# 회문인 경우 바로 0 반환
	if s == s[::-1]:
		return 0;

	for i in reversed(range(n)):
		for j in range(i+1, n):
			if s[i] == s[j]:
				dp[i][j] = dp[i+1][j-1] + 2
			else:
				dp[i][j] = max(dp[i+1][j], dp[i][j-1])
		for d in dp:
			print(d)
		print()
	
	res = n - dp[0][n-1]
	return res if res <= 3 else -1

if __name__ == '__main__':
	s = input()
	n = len(s)
	dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
	print(almost_palindrome())

'''
알고리즘:
	dp[i][j]: s[i] ~ s[j]까지의 부분 문자열 중 가장 긴 회문의 길이
	1. s[i] == s[j]인 경우: dp[i][j] = dp[i+1][j-1] + 2
		(dp[i+1][j-1]의 양 끝이 s[i], s[j]이고 두 문자는 같으므로)
	2. s[i] != s[j]인 경우: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
		(dp[i][j]에서 각각 왼쪽 끝, 오른쪽 끝 문자를 제거한 부분 문자열 중 가장 긴 회문의 길이 중 더 큰 것)
	반복문을 모두 수행하면 dp[0][n-1]에는 s의 가장 긴 회문의 길이가 저장된다.
	따라서 s의 길이에서 dp[0][n-1]을 뺀 값이 s를 회문으로 만들기 위해 제거해야 하는 최소 문자의 개수이다.
	이 값이 3보다 작거나 같은 경우에만 값을 반환하고, 그렇지 않은 경우 -1을 반환한다.

수행시간:
	중첩 반복문을 수행하므로 O(n^2)
'''
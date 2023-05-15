import sys
input = lambda: sys.stdin.readline().rstrip()

def _chicken(i, gap):
	if i > t:
		return 0
	if dp[i - gap] + 1 > dp[i]:
		dp[i] = dp[i - gap] + 1
	_chicken(i+a, a)
	_chicken(i+b, b)

def chicken(i, a, b):
	_chicken(i+a, a)
	_chicken(i+b, b)
	if dp[t] != 0:
		print(dp[t])
	else:
		cnt = 1
		for i in range(t-1, 0, -1):
			if dp[i] != 0:
				print(dp[i], cnt)
				break
			cnt += 1

if __name__ == '__main__':
	a, b, t = map(int, input().split())
	dp = [0] * (t+1)
	chicken(0, a, b)

'''
O(t^2)
'''
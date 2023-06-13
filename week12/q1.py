import sys
input = lambda: sys.stdin.readline().rstrip()

def cycle(node):
	global c

	if node == c:
		return
	dp[node] = dp[c]
	cycle(island[node])

def dfs(node):
	global c

	if dp[node] != 0:
		return dp[node]

	cur = 0
	if island[node] != -1 and not visited[island[node]]:
		visited[island[node]] = True
		cur = dfs(island[node])
	elif island[node] != -1 and dp[island[node]] == 0:
		c = island[node]
	elif island[node] != -1:
		cur = dfs(island[node])

	dp[node] = cur + 1
	if node == c:
		cycle(island[c])
		c = -1

	return dp[node]

if __name__ == '__main__':
	m, n = map(int, input().split())

	dp = [0] * (n+1)
	visited = [False] * (n+1)
	island = [-1] * (n+1)

	for _ in range(m):
		u, v = map(int, input().split())
		island[u] = v

	res = 0
	c = -1
	for i in range(n):
		if not visited[i]:
			visited[i] = True
		res = max(res, dfs(i))
	
	print(res)

import sys
input = lambda: sys.stdin.readline().rstrip()

# n
def cycle(node):
	global c

	print('cycle')

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

	print("c, node: ", c, node)

	dp[node] = cur + 1
	if node == c:
		cycle(island[c])
		c = -1

	return dp[node]

# n
if __name__ == '__main__':
	m, n = map(int, input().split())

	dp = [0] * (n+1)
	visited = [False] * (n+1)
	island = [-1] * (n+1)	# 섬이 0부터 시작하기 때문에 -1로 초기화

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

'''
알고리즘:
	dfs와 dp를 이용해 코드를 작성했다.
	우선 0번째 섬부터 dfs 함수를 호출하여 연결된 섬을 탐색한다.
	이 때 다음 섬이 방문하지 않은 상태이면 visited를 True로 바꾸고 dfs를 호출한다.
	만약 이미 dp 값이 채워져있다면 해당 값을 반환한다.
	
	연결된 섬이 있는데 dp 테이블이 채워지지 않은 경우에는 연결된 섬을 c에 저장한다(사이클 확인용).
	위 두 조건에 해당하지 않는데 연결된 섬이 있는 경우 dfs 함수를 호출한다.
	이는 초반에 사이클이 있는 경우에도 최대 방문 섬 개수를 구할 수 있게 하기 위함이다.

	이후 dp 테이블을 업데이트하고, 현재 위치한 섬과 앞서 c에 저장했던 섬이 같은 경우
	사이클이 존재한다는 의미이므로 cycle 함수를 호출해 사이클 구간의 dp 값을 업데이트한다.
	이 때 dp 값은 사이클 구간 내에서 방문 가능한 섬의 갯수이다.

	사이클에 대한 처리가 끝났으므로 c를 -1로 초기화한다.
	이 과정을 마지막 섬까지 반복한다.

수행시간:
	cycle() 함수는 최악의 경우 O(n), dfs() 함수는 최악의 경우 O(n)이다.
	두 함수를 n번씩 반복하지만 visited와 dp 테이블로 이미 방문한 섬을 확인하므로
	전체적인 코드의 시간복잡도는 O(n)이다.
'''
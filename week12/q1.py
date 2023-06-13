import sys
input = lambda: sys.stdin.readline().rstrip()

# n
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
제공된 코드의 시간 복잡도를 분석해 보겠습니다.

사이클 함수:

사이클 함수는 재귀적으로 호출됩니다. 각 호출은 섬으로 형성된 사이클의 모든 노드를 방문합니다.
최악의 경우 사이클 함수를 한 번만 호출해도 사이클의 모든 섬을 방문할 수 있으므로 시간 복잡도는 O(n)이 되며, 여기서 n은 사이클의 섬 개수입니다.
dfs 함수:

dfs 함수는 재귀적으로 호출됩니다. 주어진 노드에서 시작하여 그룹의 모든 섬을 방문합니다.
dp[node] 값이 0이 아니라면 이미 섬을 방문한 것이고, 함수는 이전에 계산한 값을 O(1) 시간 내에 반환합니다.
섬[노드]가 -1이 아니고 인접한 섬을 방문하지 않은 경우 함수는 해당 섬을 방문한 것으로 표시하고 해당 섬에 대해 재귀적으로 dfs를 호출합니다.
섬[노드]가 -1이 아니고 인접한 섬을 방문하지 않았지만 해당 섬의 dp 값이 이미 계산된 경우(0이 아닌 경우), 함수는 인접한 섬으로 c 변수를 업데이트합니다.
섬[노드]가 -1이 아니고 인접한 섬을 방문한 적이 있는 경우 함수는 재귀적으로 해당 섬의 dfs를 호출합니다.
이 함수는 dp[노드] 값을 cur + 1로 설정하며, 여기서 cur는 재귀적 호출에서 달성한 최대 깊이를 나타냅니다.
노드가 c와 같으면 함수는 섬[c]에서 순환 호출하고 c를 -1로 업데이트합니다.
dfs 함수를 한 번 호출할 때의 최악의 시간 복잡도는 O(n)이며, 여기서 n은 그룹에 있는 섬의 수입니다.
메인 부분:

메인 파트는 입력 값을 읽고 필요한 데이터 구조를 초기화합니다.
브리지 연결을 읽고 섬 목록을 업데이트하기 위해 m회 반복합니다.
res 변수는 0으로 초기화되고 c는 -1로 설정됩니다.
방문하지 않은 각 섬에서 dfs 함수를 호출하기 위해 n 범위까지 반복합니다.
각 반복에 대해 res와 dfs의 반환 값 사이의 최대값이 res에 저장됩니다.
이 부분의 시간 복잡도는 O(n)입니다.
전체적으로 제공된 코드의 시간 복잡도는 O(n)인데, 이는 그룹 또는 사이클의 최대 섬 수가 지배적인 요소이며, 이는 섬의 수와 같기 때문입니다.

Translated with www.DeepL.com/Translator (free version)


수행시간:
	cycle() 함수는 최악의 경우 O(n), dfs() 함수는 최악의 경우 O(n)이다.
	두 함수를 n번씩 반복하지만 
'''
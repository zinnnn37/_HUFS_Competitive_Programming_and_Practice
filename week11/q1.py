import sys
input = lambda: sys.stdin.readline().rstrip()

def tiling(n, k):
	dp = [[[0 for _ in range(k + 1)] for __ in range(n)] for ___ in range(n)]
	
	hor = [[0 if j < 2 else matrix[i][j-2] + matrix[i][j-1] + matrix[i][j] for j in range(n)] for i in range(n)]

	# k = 1
	for i in range(n):
		for j in range(n):
			if i == 0 and j < 2:
				dp[i][j][1] = hor[i][j]
			elif j < 2:
				dp[i][j][1] = dp[i-1][-1][1]
			else:
				dp[i][j][1] = max(dp[i][j-1][1], hor[i][j])
	
	# k > 1
	for K in range(2, k+1):
		for i in range(n):
			for j in range(n):
				if i == 0 and j <= 4:
					dp[i][j][K] = dp[i][j][K-1]
				elif j < 2:
					dp[i][j][K] = dp[i-1][-1][K]
				elif j == 2:
					dp[i][j][K] = max(dp[i-1][-1][K], dp[i-1][-1][K-1] + hor[i][j])
				elif j >= 3:
					dp[i][j][K] = max(dp[i][j-1][K], dp[i][j-3][K-1] + hor[i][j])

	print(dp[n-1][n-1][k])

if __name__ == '__main__':
	n, k = map(int, input().split())
	matrix = [list(map(int, input().split())) for _ in range(n)]

	# k개를 모두 놓을 수 없을 때
	if n // 3 * n < k:
		print(-1)
	else:
		tiling(n, k)

'''
알고리즘:
	3차원 DP테이블을 이용해 구현했다.
	우선 연산의 편리함을 위해 i-2, i-1, i 값을 더한 값을 저장하는 hor 배열을 생성한다
	그리고 dp[i][j][1]의 경우 hor의 값을 기반으로 미리 초기화한다.
	가장 첫 번째 행의 0, 1번째 인덱스의 값은 hor[i][j], 즉 0으로,
	나머지 행의 0, 1번째 인덱스의 값은 바로 전의 행 맨 마지막 인덱스의 값을 넣는다.
	나머지 행은 바로 이전 인덱스의 값과 hor[i][j]를 비교하여 더 큰 값을 넣는다.

	이후 k > 1인 경우에는 점화식을 활용해 dp 배열을 채워넣는다.
	첫 번째 행의 4번째 인덱스 까지는 타일을 두 개 놓을 수 없으므로 dp[i][j][K-1]을 넣는다
	다른 행의 0, 1번째 인덱스는 바로 위의 행 맨 마지막 인덱스의 값을 넣는다
	2번째 인덱스부터는 타일을 놓을 수 있으므로
	K번 놓았을 때의 바로 위의 행 맨 마지막 인덱스의 값(dp[i][j][K]과
	K-1번 놓았을 때의 바로 위의 행 맨 마지막 인덱스의 값(dp[i][j][K-1])
	+ 자기 자신의 값(hor[i][j]) 중 더 큰 값을 넣는다.
	나머지 인덱스의 경우 바로 앞의 값과 3번째 전의 값 + 자신의 값 중 더 큰 값을 넣는다
	모든 연산이 끝난 후 dp[n-1][n-1][k]에 구하고자 하는 값이 저장되어 있다.

수행시간:
	2차원 배열을 k번 탐색하므로 총 O(n^2 * k)만큼 소요된다.
'''
import sys
input = lambda: sys.stdin.readline().rstrip()

def drop_eggs(e, f):
	cnt = 0	# 낙하 횟수 저장

	# 목표 층에 도달 시 종료
	while dp[cnt][e] < f:
		cnt += 1
		# 점화식으로 배열 채우기
		for i in range(1, e + 1):
			print(1, end=' ')
			dp[cnt][i] = dp[cnt - 1][i - 1] + dp[cnt - 1][i] + 1
		print(dp[cnt][e])
	return cnt


if __name__ == '__main__':
	E, F = map(int, input().split())
	# dp 배열 초기화
	dp = [[0 for _ in range(E + 1)] for __ in range(F + 1)]
	print(drop_eggs(E, F))
	for d in dp:
		print(d)

'''
알고리즘:
	입력 받은 달걀의 갯수와 층수만큼의 크기로 배열을 초기화한다.
	drop_eggs() 내에서 5번의 점화식을 바탕으로 달걀의 갯수만큼 연산을 진행한다.
	이 때 dp[cnt][e]의 값이 입력 받은 층 수(F)에 도달했다면
	원하는 낙하 시도 횟수를 구한 것이므로 반복문을 종료한다.
	(f 값에 도달했을 때의 cnt가 결과)

수행시간:
	dp[i][j]는 1, 3, 7, ... 순으로 늘어나기 때문에 바깥쪽 반복문은 logF만큼 반복하고
	안쪽 반복문은 E만큼 반복하기 때문에 이 코드의 시간복잡도는 O(ElogF)이다.
'''
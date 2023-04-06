import sys
input = lambda: sys.stdin.readline().rstrip()

def drop_eggs():
	while dp[E] < F:
		for i in range(E, 0, -1):
			dp[i] += dp[i-1] + 1
		print(dp)

if __name__ == '__main__':
	E, F = map(int, input().split())
	dp = [0] * (E + 1)
	drop_eggs()
	print(dp[1])
	print(dp)

'''
알고리즘:
	입력 받은 달걀의 갯수만큼의 크기로 배열을 초기화한다.
	5, 6번 문제와 마찬가지로 dp[E]가 F에 도달할 때까지 반복문을 진행한다.
	단, 이 문제는 배열을 하나만 사용할 것을 요구하기 때문에
	이전에 구한 값을 가진 배열을 바탕으로 업데이트 시킨다.
	5, 6번 문제에서의 dp배열의 결과를 보면 dp[i][j]의 값은
	dp[i-1][j-1] + dp[i-1][j] + 1과 같다.
	이를 일차원 배열로 표현한 점화식이 dp[i] += dp[i-1] + 1이다.
	앞에서부터 진행하면 dp[i-1]의 값이 dp[i]를 구하기 전에 업데이트가 되기 때문에
	dp[i]의 값을 제대로 구할 수 없으므로 뒤에서부터 진행한다.
	이 때 dp[1]의 값은 1씩 증가하므로(dp[0]은 0이기 때문에)
	모든 반복이 끝났을 때 dp[1]의 값이 결과가 된다.

수행시간:
	dp[E]가 F가 될 때까지 반복하는데 dp[E]는 1, 3, 7, ... 씩 증가한다.
	즉, dp[E]가 F가 될 때까지 반복하는 횟수는 logF이다.
	안쪽 반복문은 E번 반복되므로 시간복잡도는 O(ElogF)이다.
'''
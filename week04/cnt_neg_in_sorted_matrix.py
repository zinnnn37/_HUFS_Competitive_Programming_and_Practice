import sys
input = lambda: sys.stdin.readline().rstrip()

def count():
	i = n - 1
	j = 0
	cnt = 0

	while i >= 0 and j < n:
		if arr[i][j] < 0:
			cnt += i + 1
			j += 1
		else:
			i -= 1
	print(cnt)

if __name__ == '__main__':
	n = int(input())
	arr = [list(map(int, input().split())) for _ in range(n)]
	count()

'''
알고리즘:
	정렬된 이차원 배열이므로 맨 마지막 행의 첫 번째 숫자부터 확인한다.
	해당 숫자가 음수라면 그 위의 열들은 모두 음수이므로
	cnt 변수에 i + 1을 더해준다(인덱스이므로 갯수를 더하기 위해서는 +1을 해준다).
	그리고 다음 숫자를 확인하기 위해 j를 1 증가시킨다.
	만약 해당 숫자가 음수가 아니라면 위쪽 열이 음수인지 확인하기 위해 i를 1 감소시킨다.

수행시간:
	반복문을 한 번 돌면서 행 혹은 열을 한 칸씩 이동하므로
	O(n + n), 즉 수행시간은 O(n)이다.
'''
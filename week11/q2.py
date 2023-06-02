import sys
input = lambda: sys.stdin.readline().rstrip()

def fold():
	pre = 0
	cur = stick[0]
	for i in range(1, n):
		if pre <= cur:
			pre = cur
			cur = stick[i]
		else:
			cur += stick[i]
	print(cur if cur > pre else pre)

if __name__ == '__main__':
	n = int(input())
	stick = list(map(int, input().split()))

	fold()

'''
알고리즘:
	현재 막대기의 길이가 이전 막대기의 길이보다 작으면 접을 수 없으므로
	현재 막대기의 길이를 이전 막대기의 길이에 더한다.
	현재 막대기의 길이가 이전 막대기의 길이보다 크거나 같으면 접을 수 있으므로
	현재 막대기의 길이를 이전 막대기의 길이로 바꾼 후 현재 막대기의 길이를 다음 막대기의 길이로 바꾼다.
	반복문이 종료된 후 현재 막대기의 길이와 이전 막대기의 길이 중 최대값을 출력한다.

	처음부터 한 번 순회를 하기 때문에 이전 값은 알 수 없어 모든 경우에 적용할 수 없다.
	따라서 5 1 2 4와 같은 값이 들어오는 경우 1과 2 사이가 접혀 답은 6이 되어야 하는데
	2와 4 사이가 접히게 되어 답이 7이 된다.

수행시간:
	fold() 함수 내에서 반복문을 한 번 사용하므로 O(n)이다.
'''
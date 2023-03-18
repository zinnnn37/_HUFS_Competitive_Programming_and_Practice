'''
리스트 A에 저장된 n개의 양의 정수 값과 목표 값 k가 입력으로 주어지면,
A의 연속된 값의 합이 k가 되는지 여부를 판별하는 코드를 작성하라

A = [2, 1, 4, 5, 3, 4, 6, 2]인 경우에,
	k = 12이면, A[2] + A[3] + A[4] = 4 + 5 + 3 = 12가 되어
	합이 12가 되는 구간이 존재한다.
	k = 14이면, 합이 14가 되는 연속된 값들의 구간이 존재하지 않는다

입력:
	첫 번째 줄: n의 값과 k의 값
		1 <= n <= 100,000, 1 <= k <= 100,000
	두 번째 줄: A의 n개의 값

출력:
	합이 k가 되는 구간이 존재하면 True, 존재하지 않으면 Falsse

주석:
	무슨 자료구조를 사용해 어떻게 해결했는지 설명하고, 수행시간 분석을 하세요

C, C++, Java 1초, Python 2초
'''

import sys
input = lambda: sys.stdin.readline().rstrip()

def partial_sum():
	left, right = 0, 0
	sum = 0

	while True:
		if sum == k:
		# 목표 합에 도달하면 True를 반환한다
			return True
		elif sum > k:
		# 목표 합보다 큰 경우 왼쪽 포인터를 1씩 증가시켜 구간합을 줄인다
			sum -= A[left]
			left += 1
		elif right == n:
		# 오른쪽 포인터가 n에 도달하는 경우 왼쪽 포인터만 움직일 수 있는데
		# sum < k이므로 목표 구간합을 찾을 수 없다(2번째 조건 불만족)
			return False
		else:
		# 오른쪽 포인터를 이동시키며 부분합을 증가시킨다
			sum += A[right]
			right += 1

if __name__	== '__main__':
	n, k = map(int, input().split())
	A = list(map(int, input().split()))
	print(partial_sum())

'''
자료구조: 배열

수행시간: O(n)
반복문을 이용해서 배열을 순차탐색하므로 O(n)시간이 걸린다
'''

'''
이차원 리스트 A에 n개의 서로 다른 양의 정수가 있다고 하자.
값 A[i][j]는 높이(해발고도)를 의미한다.
높이 A[i][j]가 상, 하, 좌, 우의 이웃 칸의 높이보다 크다면 봉우리가 된다.
	경우에 따라 이웃 칸이 2개 또는 3개일 수도 있다.
	그런 경우에는 이웃 칸의 높이보다 크면 봉우리로 정의한다.
문제는 주어진 이차원 리스트 A에 봉우리가 있다면 봉우리 하나를 찾아 출력하는 것이다.
어떻게 하면 빠르게 찾을 수 있을까?
	빠르게 찾는다는 의미는 가능하면 두 수의 비교를 되도록 적게 한다는 것이다.
'''

import sys
input = lambda: sys.stdin.readline().rstrip()

def find_peak(col, start, end):
	if start == end:
		return start
	mid = (start + end) // 2
	if arr[col][mid] > arr[col][mid + 1]:
		return find_peak(col, start, mid)
	else:
		return find_peak(col, mid + 1, end)

def find_peak_in_2D_array(srow, erow):
	if (srow == erow):
		return srow
	mrow = (srow + erow) // 2
	col = find_peak(mrow, 0, m-1)	# mid 행의 봉우리

	left = mrow - 1 >= srow and arr[col][mrow-1] > arr[col][mrow]
	right = mrow + 1 <= erow and arr[col][mrow+1] > arr[col][mrow]
	# 범위 내에 있는 경우 봉우리가 아니어도 True가 나옴
	# -> 봉우리일 때 False로 만들기

	if not left and not right:
		return [col, mrow]
	elif right: # 오른쪽이 낮을 때
		return find_peak_in_2D_array(mrow + 1, erow)
	else:
		return find_peak_in_2D_array(srow, mrow - 1)

 
if __name__ == '__main__':
	n, m = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(n)]
	print(find_peak_in_2D_array(0, n-1))
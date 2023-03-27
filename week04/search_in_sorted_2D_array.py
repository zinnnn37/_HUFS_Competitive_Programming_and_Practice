'''
입력:
	첫 줄에 n(n = 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 중 하나)과
	정후 K가 주어지고, 다음 줄부터 각 행의 n개의 값이 차례로 주어진다.
		특이하게 각 행의 값들과 각 열의 값들이 오름차순으로 정렬되어 주어진다.
	
출력:
	배열에 있는 값 중에서 K 값이 (i, j)에 있다면 i j를 차례로 출력하고
	없다면 -1을 출력한다.(행과 열은 모두 0부터 시작한다.)
	단, K값이 두 개 이상 있다면, 사전 순서로 가장 작은 (i, j)값을 출력한다.
		(a, b), (c, d) 두 위치에 대한 사전 순서는
		a < c이면 (a, b)가 앖서는 것이고,
		a == c인 경우에는 b와 d 중에서 작은 값을 갖는 것이 앞서는 것이다.
		첫 번째 샘플 입력에서 -4가 (1, 3), (2, 1), (3, 0) 모두 세 곳에 등장한다.
		사전 순서로 따지면 행 번호가 가장 작은 (1, 3)이 가장 앞서기에
		(1, 3)을 출력하면 된다.

주석:
	입력을 처리하는 시간을 제외하고 K를 탐색하는 알고리즈 부분만 설명하고
	그 부분의 수행시간을 분석한 후 Big-O로 표기하시오.

주의:
	당연히, 입력 값을 읽으면서 K를 찾으면 안된다!
	2차원 리스트에 값을 읽어 모두 저장한 후에 탐색해야 한다.
'''

import sys
sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

def	search_binary(arr, start, end):
	if start > end:
		return -1
	mid = (start + end) // 2
	if arr[mid] == K:
		return mid
	elif arr[mid] > K:
		return search_binary(arr, start, mid-1)
	else:
		return search_binary(arr, mid+1, end)

def search_matrix():
	for i in range(n):
		if arr[i][0] > K:
			break
		if arr[i][-1] < K:
			continue
		j = search_binary(arr[i], 0, n-1)
		if j != -1:
			return i, j
	return [-1]

if __name__ == '__main__':
	n, K = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(n)]
	for n in search_matrix():
		print(n, end=' ')
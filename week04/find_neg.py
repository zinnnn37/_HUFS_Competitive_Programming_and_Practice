import sys
input = lambda: sys.stdin.readline().rstrip()

def binary_search(s, e, a):
	m = (s + e) // 2
	if s == e:
		if a[m] == K:
			return m
		else:
			return -1
	if a[m] >= K:
		return binary_search(s, m, a)
	else:
		return binary_search(m+1, e, a)

def search_matrix():
	for i in range(n):
		if arr[i][0] > K:
		# 처음 값이 K보다 큰 경우
			break
		if arr[i][-1] < K:
		# 마지막 값이 K보다 작은 경우
			continue
		# 이분 탐색
		j = binary_search(0, n-1, arr[i])
		if j != -1:
			return i, j
	return [-1]

if __name__ == '__main__':
	n, K = map(int, input().split())
	arr = [list(map(int, input().split())) for _ in range(n)]
	for n in search_matrix():
		print(n, end=' ')

'''
알고리즘:
	정렬된 2차원 배열을 탐색하므로
	각 행의 첫 번째 값이 K보다 크거나 마지막 값이 K보다 작으면
	해당 행은 탐색할 필요가 없다.
	특히 첫 번째 값이 K보다 큰 경우, 정렬된 2차원 배열이므로
	해당 행 다음 행부터는 K가 존재할 가능성이 없으므로 반복문을 종료한다.
	마지막 값이 K보다 작은 경우는 다음 행에 K가 나올 가능성이 있으므로
	continue를 통해 다음 반복을 시행한다.
	위 조건에 부합하지 않는 경우, 행 내에 K가 존재할 가능성이 있으므로
	해당 행을 이분탐색을 통해 K가 있는지 확인한다.
	이분탐색 과정에서 K를 찾은 경우, 그 앞의 요소가 K일 수도 있으므로
	K를 오른쪽 끝으로 설정한 다음 다시 이분탐색을 시행한다.
	s == e인 지점이 K가 나오는 가장 첫 번째 인덱스이다.
	이 때, a[s] == K이면 해당 인덱스를 반환, 이차원 배열 내에서의 좌표를 출력하고
	a[s] != K이면 -1을 반환한 후 다음 행을 확인한다.

수행시간:
	열을 순차적으로 탐색하면서 행을 이분탐색하므로
	O(n * logn) = O(nlogn)이다.
'''
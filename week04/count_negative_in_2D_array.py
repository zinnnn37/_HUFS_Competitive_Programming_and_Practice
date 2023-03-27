'''
입력:
	첫 줄에 n(1 <= n <= 1,000)이 오고,
	다음 줄부터 각 행의 n개의 값이 차례로 주어진다.
	특이하게 각 행의 값들과 각 열의 값들이 오름차순으로 정렬되어 주어진다.

출력: 배열에 있는 음수의 개수

주석:
	입력을 처리하는 시간을 제외하고 음수를 세는 알고리즘 부분만 설명하고
	그 부분의 수행시간을 분석한 후 Big-O로 표기하시오

주의:
	입력 값을 읽으면서 음수의 개수를 세면 안된다!
	2차원 리스트의 값을 읽어 모두 저장한 후에
	각자 생각한 알고리즘에 의해 음수를 세어야 한다.
	가능하면 빠른 방법을 만들어보자.
'''

import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 8)

def binary_search_neg(start, end, i):
	if (start == end):
		return start
	mid = (start + end) // 2
	if arr[i][mid] < 0:
	# 현재 숫자가 음수인 경우
		if mid + 1 < n and arr[i][mid + 1] >= 0:
		# 다음 수가 있으며, 그 수가 음수가 아닌 경우
			return mid
		return binary_search_neg(mid + 1, end, i)
	else:
		return binary_search_neg(start, mid - 1, i)

def find_negs():
	end = n - 1	# 다음 행의 end index
	cnt = 0		# 음수의 갯수
	for i in range(n):
		if (arr[i][0] >= 0):
		# 행의 처음이 음수가 아닌 경우 확인할 필요 없음
			break;
		end = binary_search_neg(0, end, i)
		cnt += end + 1
	print(cnt)

if __name__ == '__main__':
	n = int(input())
	arr = [list(map(int, input().split())) for _ in range(n)]
	find_negs()


'''
알고리즘:
	정렬된 이차원 배열을 탐색해서 음수를 세는 것이기 때문에
	i번째 행은 i-1번째 행의 마지막 음수의 인덱스 위치까지만 확인하면 된다.
	따라서 이진탐색을 통해 얻은 마지막 음수의 인덱스 값을
	end 변수에 먼저 저장을 한 후 cnt 변수에 end + 1을 더한다.
	(인덱스 + 1이 해당 행에서의 총 음수의 갯수)
	다음 반복에서는 0번째 인덱스부터 저장된 end 인덱스까지만 탐색하면 된다.
	만약 행의 첫 번째 숫자가 음수가 아니라면
	더 이상 음수가 나오지 않기 때문에 반복문을 종료한다.

수행시간:
	n개의 행을 이진탐색하기 때문에 O(n * logn),
	즉 O(nlogn)만큼 소요된다.
'''
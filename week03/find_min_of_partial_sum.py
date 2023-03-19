'''
리스트 A에 저장된 n개의 정수 값에 대해
길이가 k인 구간(interval)을 왼쪽에서 오른쪽으로 이동하면서
해당 구간에 포함된 값 중에서 최소값을 새로운 리스트 B에 저장하라

A = [2, 1, 4, 5, 3, 4, 6, 2], k = 4인 경우에.
	첫 4개의 값 2, 1, 4, 5의 최소 값은 1,
	다음 4개의 값 1, 4, 5, 3의 최소 값은 1,
	다음 4개의 값 4, 5, 3, 4의 최소 값은 3,
	다음 4개의 값 5, 3, 4, 6의 최소 값은 3,
	다음 4개의 값 3, 4, 6, 2의 최소 값은 2가 되어
	B에는 B = [1, 1, 3, 3, 2]가 저장되어야 한다

입력
	첫 번째 줄: n의 값과 k의 값
		1 <= n <= 100,000, 1 <= k <= n
	두 번째 줄: A의 n개의 값

출력
	B의 값을 한 줄에 차례대로 출력한다
	두 수 사이에는 빈 칸 하나만 오도록 한다

주석
	무슨 자료구조를 사용해 어떻게 해결했는지 설명하고, 수행시간 분석을 하세요
'''

from math import log2
from math import ceil
import sys
sys.setrecursionlimit(10**8)
input = lambda: sys.stdin.readline().rstrip()

def init_tree(start, end, cur):
	if (start == end): # 리프노드인 경우
		tree[cur - 1] = nums[start]
		# 노드 자기 자신 넣기, 처음에 cur = 1로 시작했으므로 cur - 1이 진짜 위치
		return tree[cur - 1]
	
	mid = (start + end) // 2
	left = init_tree(start, mid, cur * 2)
	right = init_tree(mid + 1, end, cur * 2 + 1)
	tree[cur - 1] = min(left, right)
	return tree[cur - 1]

def find_min(start, end, cur, r1, r2):
	if r2 < start or r1 > end:
		return sys.maxsize
	
	if r1 <= start and end <= r2:
		return tree[cur - 1]
	
	mid = (start + end) // 2
	left = find_min(start, mid, cur * 2, r1, r2)
	right = find_min(mid + 1, end, cur * 2 + 1, r1, r2)
	return min(left, right)

def get_ans():
	ans = []
	left, right = 0, k-1
	ans.append(find_min(0, n-1, 1, 0, k-1))
	for i in range(n - k):
		left += 1
		right += 1
		if nums[left - 1] == ans[-1] or nums[right] < ans[-1]:
			if nums[left - 1] < nums[right]:
				ans.append(find_min(0, n-1, 1, left, right))
			else:
				ans.append(nums[right])
		else:
			ans.append(ans[-1])
	return ans

if __name__ == '__main__':
	n, k = map(int, input().split())
	nums = list(map(int, input().split()))
	tree = [0] * (pow(2, ceil(log2(n) + 1)) - 1)
	init_tree(0, n-1, 1)
	ans = get_ans()
	
	for v in ans:
		print(v, end=' ')
'''
자료구조: 세그먼트 트리
세그먼트 트리는 특정 구간 내에서 특정 작업을 수행할 때 효율적인 알고리즘이다.
이 문제의 경우 부모 노드는 자식 노드 중 더 작은 값을 가지도록 한다.
이진트리의 노드 수는 2^(h) - 1개, h는 log2(n) + 1이므로
노드 수가 2^(log2(n) + 1) - 1개인 트리를 만든다.

우선 init_tree()를 통해 트리를 초기화하는데,
리프노드에는 입력받은 배열을 차례대로 넣고(start == end인 경우)
부모노드에는 자식 노드 중 작은 값을 넣는다

find_min()은 구간의 최소값을 찾는 함수이다.
만약 start와 end가 주어진 범위 내에 있으면 현재 노드를 반환하고
그렇지 않으면 sys.maxsize를 반환한다.
재귀가 모두 끝난 후 반환되는 노드가 구간의 최소값이 된다.

get_ans()는 구간의 최소값 배열을 반환한다.
우선 find_min()으로 가장 첫 구간의 최소값만 구한 후,
두 개의 포인터를 이용해 나머지 구간의 최소값을 구한다.
left와 right는 구간의 가장 첫 노드와 마지막 노드를 가리킨다.
find_min()을 통해 첫 구간의 최소값만을 구한 후
left와 right를 오른쪽으로 한 칸씩 움직이면서 다음 구간의 최소값을 구한다.
만약 left-1(구간을 벗어난 수)이 최소값이거나
right(구간에 들어온 수)가 최소값보다 작다면 두 수의 크기를 비교하여 맞는 연산을 수행한다.
만약 left-1이 더 작은 경우 find_min()을 통해 구간의 최소값을 구한다.
right가 더 작은 경우에는 필연적으로 right가 최소값이 되므로
right의 값을 ans에 append()한다.

수행시간: O(n)
세그먼트 트리는 이진 트리이므로 초기화하고 검색을 하는데 O(logn)시간이 걸린다.
검색을 총 한 번 진행한 후, nums 배열을 한 번 n - k번 탐색하므로
전체 코드의 시간복잡도는 O(logn + n)시간, 즉, O(logn)이다.
'''
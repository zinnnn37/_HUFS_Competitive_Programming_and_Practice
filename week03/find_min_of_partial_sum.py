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
	# 왼쪽 자식 노드부터 재귀적으로 함수 수행
	tree[cur - 1] = min(left, right)
	return tree[cur - 1]
	# 자식 노드 중 더 작은 노드 반환

def find_min(start, end, cur, r1, r2):
	if r2 < start or r1 > end:
	# 구간이 겹치지 않는 경우 최대값 반환
		return sys.maxsize
	
	if r1 <= start and end <= r2:
	# 구간이 겹칠 때 현재 노드 반환
		return tree[cur - 1]
	
	mid = (start + end) // 2
	left = find_min(start, mid, cur * 2, r1, r2)
	right = find_min(mid + 1, end, cur * 2 + 1, r1, r2)
	return min(left, right)
	# 자식 노드 중 더 작은 노드 반환

if __name__ == '__main__':
	n, k = map(int, input().split())
	nums = list(map(int, input().split()))
	tree = [0] * (pow(2, ceil(log2(n) + 1)) - 1)
	ans = []
	init_tree(0, n-1, 1)
	for i in range(n-k+1):
		ans.append(find_min(0, n-1, 1, i, i+k-1))
	for v in ans:
		print(v, end=' ')
	

'''
자료구조: 세그먼트 트리
세그먼트 트리는 특정 구간 내에서 어떠한 작업을 수행할 때 효율적인 알고리즘이다.
이 문제의 경우 최소값 찾기를 수행하므로,
부모 노드는 두 자식 노드 중 더 작은 값을 가지게 된다.

이진트리의 총 노드 수는 2^(h) - 1개, h는 log2(n) + 1이므로
노드 수가 2^(log2(n) + 1) - 1개인 트리를 만들면 된다

우선 init_tree()를 통해 트리를 초기화시켜주는데,
리프노드에 도달할 때까지 재귀를 돌며
리프노드에 입력받은 배열을 차례대로 넣는다(start == end인 경우)
차례대로 재귀를 빠져나오면서 부모노드에 두 자식 노드 중 더 작은 값을 넣는다
결과적으로 루트 노드에는 배열 전체의 최소값이 담기게 된다.

이후 find_min()을 통해 재귀적으로 최소값을 구한다.
만약 현재의 start와 end의 값이 구간 내에 존재한다면 현재 노드를 반환한다.
현재 노드는 리프 노드가 아닐 수 있다.
재귀가 모두 끝난 후 반환되는 노드가 구간의 최소값이 된다.

이 때, 입력받은 배열의 왼쪽에서부터 오른쪽으로 이동하면서
길이가 k인 부분 배열을 확인해야 하므로, 
0부터 n - k + 1까지 반복문을 돌며 모든 구간의 최소값을 구한다.

---------------

수행시간: O(nlogn)
세그먼트 트리는 이진 트리이므로 초기화하고 검색을 하는데 O(logn)시간이 걸린다.
그리고 검색을 총 n-k+1번 반복하므로 O((logn) * (n - k + 1))시간,
즉, 전체 코드의 시간복잡도는 O(nlogn)이다.
'''


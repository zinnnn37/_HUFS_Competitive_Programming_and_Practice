import sys
input = lambda: sys.stdin.readline().rstrip()

def init(node, s, e):
	if s == e:
		bit[node] = 1
		return bit[node]
	mid = (s + e) // 2
	bit[node] = init(node * 2, s, mid) + init(node * 2 + 1, mid + 1, e)
	return bit[node]

def update(node, s, e, idx, diff):
	if idx < s or idx > e:
		return
	bit[node] += diff
	if s != e:
		mid = (s + e) // 2
		update(node * 2, s, mid, idx, diff)
		update(node * 2 + 1, mid + 1, e, idx, diff)

def query(node, s, e, k):
	if s == e:
		return s
	
	mid = (s + e) // 2
	left = bit[node * 2]

	if left >= k:
		return query(node * 2, s, mid, k)
	return query(node * 2 + 1, mid + 1, e, k - left)

if __name__ == '__main__':
	B = [int(x) + 1 for x in input().split()]
	n = len(B)
	bit = [0] * (n * 4)
	init(1, 0, n - 1)

	A = [0] * n

	for i in range(n-1, -1, -1):
		idx = query(1, 0, n-1, B[i])
		A[i] = idx
		update(1, 0, n-1, idx, -1)
	print(A)

'''
알고리즘:
	세그먼트 트리를 이용하여 리스트 B의 뒤쪽부터 하나씩 확인하면서 A를 채워나간다.
	query 함수로 어떤 수를 채워넣을지 결정하고, update 함수로 이미 사용한 수는 0으로 만든다.
	각 노드의 부모 노드는 자식 노드의 합을 저장한다.
	이 때 리프노드는 1로 초기화하기 때문에 각 노드는 자신의 자식 노드의 개수를 저장하게 된다.

	query 함수에서는
	k번째 노드(B[i])를 확인하여 리프노드에 도달하면 그 노드의 인덱스를 반환한다.
	리프노드가 아니라면 왼쪽 자식 노드의 개수를 확인하여 k가 작거나 같으면 왼쪽 자식 노드로,
	크면 오른쪽 자식 노드로 이동한다.
	오른쪽 자식 노드로 이동할 때, s가 mid + 1로 변하므로
	k에서 왼쪽 자식 노드의 개수를 빼주어 mid + 1 ~ e 구간에서만 확인하면 되는 1의 수를 전달한다.

	update 함수에서는 확인한 인덱스의 노드를 0으로 만든다.
	0으로 수정한 노드의 부모노드들도 1씩 감소시켜 구간 내에서 사용할 수 있는 노드의 개수를 갱신한다.

수행시간:
	반복문을 n번만큼 돌면서 query와 update를 호출하는데,
	query와 update는 각각 log(n)번만큼 돌기 때문에
	총 수행시간은 O(nlogn)이다.
'''
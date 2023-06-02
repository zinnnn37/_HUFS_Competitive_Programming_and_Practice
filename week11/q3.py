import sys
input = lambda: sys.stdin.readline().rstrip()

def sol(n, value, price):
	l_max = [0] * (n+2)	# prefix
	r_max = [0] * (n+2)	# suffix

	for i in range(1, n+1):
		l_max[i] = max(l_max[i-1], abs(value[i] - price[i]))
	
	for i in range(n, 0, -1):
		r_max[i] = max(r_max[i+1], abs(value[i] - price[i]))
	
	ll_max = [0] * (n+2)	# prefix without i
	rr_max = [0] * (n+2)	# suffix without i

	for i in range(2, n+1):
		ll_max[i] = min(l_max[i-1], max(ll_max[i-1], abs(value[i-1] - price[i])))

	for i in range(n-1, 0, -1):
		rr_max[i] = min(r_max[i+1], max(rr_max[i+1], abs(value[i+1] - price[i])))

	ans = [0] * (n+1)

	for i in range(1, n+1):
		ans[i] = min(max(ll_max[i], r_max[i+1]), max(l_max[i-1], rr_max[i]))

	idx = 1

	for i in range(2, n+1):
		if ans[i] < ans[idx]:
			idx = i
	
	return value[idx]

if __name__ == '__main__':
	n = int(input())
	value = [0] + list(map(int, input().split()))
	price = [0] + list(map(int, input().split()))

	value.sort()
	price.sort()

	print(sol(n, value, price))

'''
알고리즘:
	우선 value와 price를 정렬한다.
	
	l_max는 i까지의 최대값, r_max는 i부터의 최대값을 저장한다.
	이 때 최대값은 i번째 가격과 가치 차의 절댓값이다.

	ll_max는 i-1 까지의 최대값, rr_max는 i+1 부터의 최대값을 저장한다.
	(i번째 상품을 빼는 경우)
	ll_max는 i-1번째 가치와 i번째 가격의 절댓값을,
	rr_max는 i+1번째 가치와 i번째 가격의 절댓값을 저장한다.
	
	ans는 가격과 가치의 차이의 최대값 중 최소값을 저장한다.
	i번째 상품을 뺐을 때 왼쪽 부분 리스트의 매칭을 이동시킨 ll_max[i]와
	같은 위치의 가격과 가치 차를 저장하는 r_max[i+1] 중 최대값과
	i번째 상품을 뺐을 때 오른쪽 부분 리스트의 매칭을 이동시킨 rr_max[i]와
	같은 위치의 가격과 가치 차를 저장하는 l_max[i-1] 중 최대값을 비교하여
	둘 중 더 작은 값을 ans[i]에 저장한다(최댓값의 최소값).

	이후 ans를 순회하며 차이가 가장 큰 요소의 인덱스를 저장한다.
	이 인덱스가 최종적으로 빼야 할 상품의 인덱스가 된다.

수행시간:
	value와 price를 정렬하는 데 O(nlogn)시간이 소요되고
	sol() 함수에서 6개의 for문을 사용하여 O(6n)시간이 소요된다.
	따라서 총 수행시간은 O(nlogn)이다.
'''
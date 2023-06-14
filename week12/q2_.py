import sys
input = lambda: sys.stdin.readline().rstrip()

def query(x, k):
	res = x
	for _ in range(k):
		res = f[res - 1]
	return res

if __name__ == '__main__':
	m = int(input())
	f = list(map(int, input().split()))

	for _ in range(int(input())):
		x, k = map(int, input().split())
		print(query(x, k))

'''
알고리즘:
	입력되는 쿼리마다 query 함수를 호출한다.
	qurey 함수는 x를 k번 계산한 값을 반환한다.

수행시간:
	query 함수는 O(k)이고 쿼리의 수는 q이므로
	총 수행시간은 O(qk)이다.
'''
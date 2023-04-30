import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**8)

def almost_palindrome(start, end, cnt):
	if cnt > 3:
		return -1
	if start >= end:
		return cnt
	if s[start] == s[end]:
		return almost_palindrome(start+1, end-1, cnt)
	elif s[start] != s[end]:
		l = almost_palindrome(start+1, end, cnt+1)
		r = almost_palindrome(start, end-1, cnt+1)
		if l == -1 and r == -1:
			return -1
		elif l == -1:
			return r
		elif r == -1:
			return l
		else:
			return min(l, r)
	return cnt

if __name__ == '__main__':
	s = input()
	n = len(s)
	print(almost_palindrome(0, n-1, 0))

'''
알고리즘:
	재귀함수를 이용하여 오른쪽과 왼쪽 끝을 비교한다.
	1. 두 문자가 같은 경우: 왼쪽 끝과 오른쪽 끝을 제거한 부분 문자열을 재귀적으로 호출한다.
		이 때 cnt는 그대로 전달한다.
	2. 두 문자가 다른 경우: 왼쪽 끝을 제거한 부분 문자열과 오른쪽 끝을 제거한 부분 문자열의 결과 중
		더 작은 값을 반환하는데, 만약 하나의 값만 -1을 반환하는 경우에는 -1이 아닌 값이 반환되고
		둘 다 -1을 반환하는 경우에는 -1을 반환한다.
	cnt가 3보다 크거나 start가 end보다 크거나 같은 경우 더 이상 비교할 필요가 없으므로
	각각 -1과 cnt를 반환한다.

수행시간:
	없앨 수 있는 문자는 최대 3개이므로 재귀 분기는 최대 8번까지 생긴다.
	따라서 평균적인 시간복잡도는 O(n)이다.
'''
import sys
sys.setrecursionlimit(10**8)
input = lambda: sys.stdin.readline().rstrip()

def LPS(str, s, e):
	if s > e:	# 비교 끝
		return 0
	if s == e:	# 홀수
		return 1
	if str[s] == str[e]:
		return LPS(str, s + 1, e - 1) + 2
	else:
		left = LPS(str, s, e - 1)
		right = LPS(str, s + 1, e)
		return max(left, right)
		# 양 끝 중 하나만 제외한 부분수열 중 더 큰 회문 길이 반환

if __name__ == '__main__':
	s = input()

	print(LPS(s, 0, len(s) - 1))
import math
import sys
input = lambda: sys.stdin.readline().rstrip()

def guess_two_missing_numbers(n, S, T):
	s1 = (n * (n + 1)) // 2 - S
	s2 = n * (n + 1) * (2 * n + 1) // 6 - T
	# 자연수 거듭제곱의 합 공식을 이용해 1 + ... + n 과 1^2 + ... + n^2 을 구한 후,
	# S와 T를 빼어 a + b의 값과 a^2 + b^2의 값을 구한다 (각각 s1과 s2)
	x = int(math.pow(s1, 2) - s2)
	# (a + b)^2 = a^2 + 2ab + b^2이므로 s1^2 - s2 = 2ab (2ab는 x로 표기한다)
	a = int((2 * s1 + math.sqrt(4 * math.pow(s1, 2) - 8 * x)) // 4)
	# a + b = s1 이므로 b = s1 - a
	# x = 2a(s1 - a) 이므로 2a^2 - 2a * s1 + x = 0 이라는 이차방정식을 얻을 수 있다.
	# 근의 공식을 이용해 양수의 해를 구한다.
	b = s1 - a
	# a + b = s1, b = s1 - a
	# a의 값을 구했으므로 b의 값 또한 구할 수 있다.
	return (a, b) if a < b else (b, a)  # a < b are two missing numbers

n = int(input())
S, T = [int(x) for x in input().split()]
a, b = guess_two_missing_numbers(n, S, T)
print(a, b)
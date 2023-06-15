import math
import sys
input = lambda: sys.stdin.readline().rstrip()

def guess_two_missing_numbers(n, S, T):
	s1 = (n * (n + 1)) // 2 - S
	s2 = n * (n + 1) * (2 * n + 1) // 6 - T
	x = int(math.pow(s1, 2) - s2)
	a = int((2 * s1 + math.sqrt(4 * math.pow(s1, 2) - 8 * x)) // 4)
	b = s1 - a
	return (a, b) if a < b else (b, a)

n = int(input())
S, T = [int(x) for x in input().split()]
a, b = guess_two_missing_numbers(n, S, T)
print(a, b)
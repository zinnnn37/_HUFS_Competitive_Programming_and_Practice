import sys
input = lambda: sys.stdin.readline().rstrip()

def fold():
	pre = stick[0]
	cur = stick[1]
	for i in range(2, n):
		if pre <= cur:
			pre = cur
			cur = stick[i]
		else:
			cur += stick[i]
	print(cur if cur > pre else pre)

if __name__ == '__main__':
	n = int(input())
	stick = list(map(int, input().split()))

	fold()
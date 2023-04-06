'''import math

def isSafe(h):
    if h < answer :
        return True
    return False

def twoEggsDrop(n):
    cnt = 0
    sqrt_n = int(math.floor(math.sqrt(n)))
    for h in range(sqrt_n, n+1, sqrt_n):
        cnt += 1
        print(h)
        if not isSafe(h):
            break
    for h2 in range(h-sqrt_n+1, h):
        cnt += 1
        if not isSafe(h2):
            return cnt
    return cnt

n = int(input())
answer = 24
print(answer, twoEggsDrop(n))
'''

import sys
INT_MAX = sys.maxsize

def drop_eggs(n, k):
	eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]

	for i in range(1, n + 1):
		eggFloor[i][1] = 1
		eggFloor[i][0] = 0

	for j in range(1, k + 1):
		eggFloor[1][j] = j

	for i in range(2, n + 1):
		for j in range(2, k + 1):
			eggFloor[i][j] = INT_MAX
			for x in range(1, j + 1):
				res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
				if res < eggFloor[i][j]:
					eggFloor[i][j] = res
	print(eggFloor)
	return eggFloor[n][k]

if __name__ == "__main__":
	E, F = map(int, input().split())
	print(drop_eggs(E, F))
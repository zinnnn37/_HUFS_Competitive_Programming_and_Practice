import math
import random

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
answer = random.randint(1, n)
answer = 24
print(answer, twoEggsDrop(n))
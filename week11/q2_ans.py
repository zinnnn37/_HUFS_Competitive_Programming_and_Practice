import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()

def sol():
    pre = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + stick[i - 1]

    INF = sys.maxsize
    dp = [INF for _ in range(n + 1)]

    h = [(0, 0)]
    for i in range(1, n + 1):
        j = 0
        while h and h[0][0] <= pre[i]:
            j = max(j, heapq.heappop(h)[1])
        dp[i] = pre[i] - pre[j]
        heapq.heappush(h, (dp[j] + pre[j], j))
        heapq.heappush(h, (dp[i] + pre[i], i))

    ans = min(max(dp[i], pre[n] - pre[i]) for i in range(1, n + 1))
    return ans

if __name__ == '__main__':
    n = int(input())
    stick = list(map(int, input().split()))
    print(sol())
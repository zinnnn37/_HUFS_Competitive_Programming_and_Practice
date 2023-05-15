import sys
input = lambda: sys.stdin.readline().rstrip()

def chicken():
    for i in range(t + 1):
        if dp[i] != 0:
            if i + a <= t:
                if dp[i] + 1 > dp[i + a]:
                    dp[i + a] = dp[i] + 1
            if i + b <= t:
                if dp[i] + 1 > dp[i + b]:
                    dp[i + b] = dp[i] + 1
    if dp[t] != 0:
        print(dp[t])
    else:
        cnt = 1
        for i in range(t-1, 0, -1):
            if dp[i] != 0:
                print(dp[i], cnt)
                break
            cnt += 1

if __name__ == '__main__':
    a, b, t = map(int, input().split())
    dp = [0] * (t + 1)
    dp[a], dp[b] = 1, 1

    chicken()

'''
알고리즘:
    후라이드 치킨과 양념 치킨 각각을 먼저 먹었을 때(dp[a], dp[b])를 1로 초기화한다.
    이후 반복문을 돌면서 0이 아닌 구간이 나오면(치킨을 다 먹었을 시점)
    그 시점부터 각각 a 만큼 뒤의 인덱스와 b 만큼 뒤의 인덱스의 값을 확인하여
    확인한 값보다 dp[i] + 1이 더 크다면 값을 업데이트 한다.
    만약 dp[t]가 0이 아니라면 정확히 t분에 치킨만을 먹을 수 있으므로 d[t]를 출력하고
    0이라면 정확히 t분에 치킨만 먹는 것이 불가능한 것이므로
    dp[t-1]부터 차례로 확인하며 0이 아닌 마지막 값을 출력한다.
    이 때 cnt도 1씩 증가시키며 남은 시간도 함께 출력한다.

수행 시간:
    크게 t+1번 반복하는 반복문 하나와 t-1번 반복하는 반복문 하나로 구성되므로
    총 수행시간은 O(2t) = O(t)이다.
'''
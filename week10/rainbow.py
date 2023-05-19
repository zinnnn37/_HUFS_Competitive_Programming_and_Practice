import sys
input = lambda: sys.stdin.readline().rstrip()

def dp():
    s, e = 0, 0
    ans = sys.maxsize
    for i in range(n):
        if check1[rainbow[i]] != 0 and rainbow[s] == rainbow[i]:
            s += 1
            e += 1
        else:
            check1[rainbow[i]] += 1
            check2[rainbow[i]] -= 1
            e += 1
        if check1[1:].count(0) == 0 and check2[1:].count(0) == 0:
            if sum(check1) < ans:
                ans = sum(check1)
    print(ans if ans != sys.maxsize else 0)

if __name__ == '__main__':
    n, k = map(int, input().split())
    check1 = [0] * (k + 1)
    check2 = [0] * (k + 1)
    rainbow = [0] * n
    for i in range(n):
        x = int(input())
        rainbow[i] = x
        check2[x] += 1

    dp()

'''
s, e, idx_in, idx_out
idx* -> 구간 내 색이 다 나온 경우

color[k] > 3개
flag -> p' 내에 모두 나오는 것 확인

1 2 3 1 1 4 2 4 3
-> end 이동하며 color[k] 갱신
idx_in은 color[k]가 0이었던 경우에만 +1
=> p'만 확인
if idx_in == k: flag = True
이 때의 p' 길이를 저장해놓기(ans)

만약 s부터 확인해서 color[s]가 1보다 크면 s += 1, color[s-1] -= 1
하고 idx_out에 color[s-1]을 반영
> 시작하기 전에 idx_out이랑 color2 값 다 넣어놓고 시작하는 게 좋을 듯?

idx_in과 idx_out 모두 k일 때 쌍무지개
ans는 계속 돌면서 .. in과 out이 모두 k일 때 ans 갱신(작은 걸로)
'''

import sys
input = lambda: sys.stdin.readline().rstrip()

def double_rainbow():
    global fin, fout
    s, e = 0, 0
    ans = sys.maxsize
    while s <= e and s < n:
        if check1[rainbow[s]] > 1:
            check1[rainbow[s]] -= 1
            if check2[rainbow[s]] == 0:
                fout += 1
            check2[rainbow[s]] += 1
            s += 1
        elif e == n:
            check1[rainbow[s]] -= 1
            if check1[rainbow[s]] == 0:
                fin -= 1
            if check2[rainbow[s]] == 0:
                fout += 1
            check2[rainbow[s]] += 1
            s += 1
        elif e < n:
            if check1[rainbow[e]] == 0:
                fin += 1
            check1[rainbow[e]] += 1
            check2[rainbow[e]] -= 1
            if check2[rainbow[e]] == 0:
                fout -= 1
            e += 1
        if fin == fout == k:
            ans = min(ans, e - s)
    print(ans if ans != sys.maxsize else 0)

if __name__ == '__main__':
    n, k = map(int, input().split())
    check1 = [0] * (k + 1)
    check2 = [0] * (k + 1)
    fin, fout = 0, 0
    rainbow = [0] * n
    for i in range(n):
        x = int(input())
        if check2[x] == 0:
            fout += 1
        rainbow[i] = x
        check2[x] += 1
    double_rainbow()

'''
알고리즘:
    투포인터를 이용해 구간 내에서 색이 다 나오는지 확인한다.
    check 배열들이 각각의 색이 집합에 얼만큼 나오는지를 저장하는 배열이고
    fin과 fout은 두 집합에 각각 몇 개의 색이 있는지를 저장하는 변수이다.
    
    double_rainbow() 함수를 실행하기 전인 경우,
    P는 비어있는 집합이고 P-P'은 모든 점을 포함하는 집합이므로
    입력을 받으면서 check2 배열과 fout 변수를 업데이트 한다.(둘 다 P-P'와 관련된 변수)
    이 때, 입력되는 색의 값이 check2의 인덱스가 되기 때문에 입력을 받으며 1씩 증가시키는 것이다.
    그리고 check2 배열을 업데이트 할 때, 해당 인덱스의 값이 0이었다면
    새로운 색이 입력되는 것이므로 fout 변수를 1 증가시킨다.
    
    double_rainbow 함수는 쌍무지개인지 확인하는 함수이다.
    투 포인터를 사용하므로 s가 e보다 작거나 클 때, 그리고 s가 n보다 작을 때만 실행한다.
    먼저 e를 오른쪽으로 움직이면서 check1 배열과 check2 배열을 업데이트 한다.
    만약 새로 가리키는 색깔이 P'에 없는 색이라면 fin 변수를 1 증가시키고
    check1 배열의 해당 인덱스를 1 증가시킨다.
    그리고 check2 배열의 해당 인덱스를 1 감소시킨다.
    만약 check2 배열의 인덱스가 0이 되었다면 포함되지 않은 색이 하나 생긴 것이므로
    fout 변수를 1 감소시킨 후 e를 1 증가시킨다.
    만약 s가 가리키는 색깔이 P'에 중복되었다면 check1 배열의 해당 인덱스를 1 감소시킨다.
    그리고 check2 배열의 해당 인덱스를 1 증가시킨다.
    만약 check2의 해당 인덱스가 0이었다면 새로운 색이 추가된 것이므로
    fout 변수를 1 증가시킨 후 s를 1 증가시킨다.
    e가 n에 다다랐다면 s만 증가시키면서 check1 배열과 check2 배열을 업데이트 한다.
    연산은 앞에서 설명했던 것과 동일하게 진행한다.
    
    위 연산이 수행되고 나면 fin과 fout이 모두 k가 되었는지 확인한다.
    만약 둘 다 k가 되었다면 ans를 갱신한다.
    이 때 ans는 기존에 저장되어 있던 값과 e-s의 값 중 작은 것으로 갱신한다.
    초기값이 sys.maxsize이기 때문에 ans가 갱신되지 않았다면 0을 출력하고
    그렇지 않다면 ans를 출력한다.
    
수행시간:
    s와 e가 각각 오른쪽으로 n번 이동하므로 O(2n) = O(n)이다.
'''
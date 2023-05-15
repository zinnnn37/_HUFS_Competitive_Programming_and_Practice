import sys
input = lambda: sys.stdin.readline().rstrip()

def LCS(s, r):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == r[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[n][n]
    

if __name__ == '__main__':
    s = input()
    r = s[::-1]  # 입력받은 문자열을 뒤집음
    print(LCS(s, r))


'''
알고리즘:
	입력 받은 문자열 s와 이를 뒤집은 r을 이용해 구한 LCS가
	곧 최장 회문 부수열이 된다.
	이중 반복문을 돌면서 s[i-1]와 r[j-1]의 문자가 같은 경우
	dp[i][j]는 dp[i-1][j-1]의 값에 1을 더한 값이 된다(LCS가 1만큼 늘어남)
	일치하지 않는 경우는 s의 이전 인덱스까지의 LCS
	혹은 r의 이전 인덱스까지의 LCS를 비교한다.
	둘 중 더 큰 수가 dp[i][j] 값이 된다.
	i와 j 모두 n까지 반복하므로 dp[n][n]에 결과가 저장된다.
	이 값이 최장 회문 부수열이다.

수행 시간:
	n만큼 반복하는 반복문이 2번 중첩되어 있으므로
	총 수행시간은 O(n^2)이다.
'''
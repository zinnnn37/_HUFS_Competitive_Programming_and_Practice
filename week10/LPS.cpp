#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
 
// 최장 회문 길이 구하기
int LCS(string str, string rev, int n, vector<vector<int>> &dp)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            // str과 rev의 문자가 같은 경우 +1
            if (str[i - 1] == rev[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            }
            // 일치하지 않는 경우 왼쪽 혹은 오른쪽 중 더 긴 회문을 가지고 있는 경우
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

	// for (int i = 1; i <= n; i++)
	// {
	// 	for (int j = 1; j <= n; j++)
	// 		cout << dp[i][j] << " ";
	// 	cout << endl;
	// }
 
    return dp[n][n];
}
 
int main()
{
	string str;
	cin >> str;
 
    int n = str.length();
 
    // LCS 길이 저장용
    vector<vector<int>> dp(n + 1, vector<int>(n + 1));
 
	// 입력받은 문자 반전
    string rev = str;
    reverse(rev.begin(), rev.end());
 
    // LCS로 LPS 찾기
    cout << LCS(str, rev, n, dp) << endl;
 
    return 0;
}

/*
알고리즘:
	입력 받은 문자열 str과 이를 뒤집은 rev를 이용해 구한 LCS가
	곧 최장 회문 부수열이 된다.
	이중 반복문을 돌면서 str[i-1]와 rev[j-1]의 문자가 같은 경우
	dp[i][j]는 dp[i-1][j-1]의 값에 1을 더한 값이 된다(LCS가 1만큼 늘어남)
	일치하지 않는 경우는 str의 이전 인덱스까지의 LCS
	혹은 rev의 이전 인덱스까지의 LCS를 비교한다.
	둘 중 더 큰 수가 dp[i][j] 값이 된다.
	i와 j 모두 n까지 반복하므로 dp[n][n]에 결과가 저장된다.
	이 값이 최장 회문 부수열이다.

수행 시간:
	n만큼 반복하는 반복문이 2번 중첩되어 있으므로
	총 수행시간은 O(n^2)이다.
*/
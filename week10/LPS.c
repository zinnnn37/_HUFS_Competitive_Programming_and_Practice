#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int	LPS(char *s)
{
	int	n, j, ans;
	n = strlen(s);
	
	int dp[n][n];

	for (int i = 0; i < n; i++)
		dp[i][i] = 1;
	
	for (int i = 0; i < n - 1; i++)
		if (s[i] == s[i + 1])
			dp[i][i + 1] = 2;
	
	for (int k = 2; k < n + 1; k++)
	{
		for (int i = 0; i < n - k + 1; i++)
		{
			j = i + k - 1;
			if (s[i] == s[j])
				dp[i][j] = dp[i + 1][j - 1] + 2;
			else
				dp[i][j] = MAX(dp[i][j - 1], dp[i + 1][j]);
		}
	}
	ans = dp[0][n - 1];
	return (ans);
}

int	main(void)
{
	char	*s;

	scanf("%s", s);
	
	printf("%d\n", LPS(s));
	return (0);
}
// 구름에서 실행 안됨................
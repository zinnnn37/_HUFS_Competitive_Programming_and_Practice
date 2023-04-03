#include <stdio.h>

#define MAX(x, y) (x > y) ? x : y
#define INT_MAX 2147483647

int	drop_eggs(int e, int f)
{
	int	matrix[e + 1][f + 1];
	int	ans;
	
	for (int i = 0; i <= e; i++)
	{
		matrix[i][1] = 1;
		matrix[i][0] = 0;
	}
	for (int i = 0; i <= f; i++)
		matrix[1][i] = i;
	
	for (int i = 2; i <= e; i++)
	{
		for (int j = 2; j <= f; j++)
		{
			matrix[i][j] = INT_MAX;
			for (int k = 1; k <= j; k++)
			{
				ans = MAX(matrix[i - 1][k -1], matrix[i][j - k]) + 1;
				if (ans < matrix[i][j])
					matrix[i][j] = ans;
			}
		}
	} 
	return matrix[e][f];
}

int	main(void)
{
	int E, F, ans;

	scanf("%d %d", &E, &F);
	printf("%d\n", drop_eggs(E, F));
}
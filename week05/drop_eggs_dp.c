#include <stdio.h>
#include <limits.h>

int	max(int x, int y)
{
	return (x > y) ? x : y;
}

int drop_eggs(int e, int f)
{
	int matrix[e + 1][f + 1];
	int res;
	int i, j, k;

	for (i = 1; i <= e; i++) {
		matrix[i][1] = 1;
		matrix[i][0] = 0;
	}
	for (j = 1; j <= f; j++)
		matrix[1][j] = j;
 
	for (i = 2; i <= e; i++) {
		for (j = 2; j <= f; j++) {
			matrix[i][j] = INT_MAX;
			for (k = 1; k <= j; k++) {
				res = MAX(matrix[i - 1][k - 1], matrix[i][j - k]) + 1;
				if (res < matrix[i][j])
					matrix[i][j] = res;
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
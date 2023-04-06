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

	// 초기값 설정
	for (int i = 1; i <= e; i++)
		matrix[i][1] = 1;
	for (int j = 1; j <= f; j++)
		matrix[1][j] = j;

	for (int i = 2; i <= e; i++)
	{
		for (int j = 2; j <= f; j++)
		{
			// min 연산을 위한 초기화
			matrix[i][j] = INT_MAX;
			for (int k = 1; k <= j; k++)
			{
				// 점화식 바탕으로 연산
				res = max(matrix[i - 1][k - 1], matrix[i][j - k]) + 1;
				if (res < matrix[i][j])
					matrix[i][j] = res;
			}
		}
	}
	return matrix[e][f];
}

int	main(void)
{
	int E, F;

	scanf("%d %d", &E, &F);
	printf("%d\n", drop_eggs(E, F));
	return 0;
}

/*
알고리즘:
	[E+1][F+1] 크기의 정수 배열을 선언하고 초기화한다.
	달걀이 몇 개가 있든 1층은 한 번에 확인 가능하므로 [E][1] = 0,
	달걀이 한 개일 때는 낮은 층부터 한 층씩 확인해야하므로 [1][F] = F로 초가화한다.
	i는 달걀의 갯수, j는 층수, k는 j-1부터 한 층씩 내려가면서 확인하기 위한 변수이다.
	res와 matrix[i][j]에 저장된 값 중 최소값이 최종 값이 되므로
	matrix[i][j]의 초기값을 INT_MAX로 지정한다.
	가장 안쪽 반복문 내에서 3번에서 구한 점화식을 바탕으로 matrix[i][j]에 값을 넣는다.
	모든 과정이 끝난 후 matrix[E][F]의 값을 반환한다.

수행시간:
	3중 반복문 내에서 각각의 계란 갯수에 따른 낙하 횟수를 확인할 때 F^2번 반복한다.
	(가장 바깥 반복문 E-1번, 그 다음 반복문 F-1번, 가장 안쪽 반복문 j번(F)) 
	따라서 시간복잡도는 O(E * F^2)이다.
*/
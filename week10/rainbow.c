#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100000

int check1[MAX_SIZE + 1];
int check2[MAX_SIZE + 1];
int rainbow[MAX_SIZE];

int min(int a, int b) {
    return (a < b) ? a : b;
}

void dp(int n, int k) {
    int s = 0, e = 0;
    int ans = MAX_SIZE;
    int i;

    for (i = 0; i < n; i++) {
        if (check1[rainbow[i]] != 0 && rainbow[s] == rainbow[i]) {
            s += 1;
            e += 1;
        } else {
            check1[rainbow[i]] += 1;
            check2[rainbow[i]] -= 1;
            e += 1;
        }

        int count1 = 0, count2 = 0;
        for (int j = 1; j <= k; j++) {
            if (check1[j] == 0) count1++;
            if (check2[j] == 0) count2++;
        }

        if (count1 == 0 && count2 == 0) {
            if (sum(check1, k + 1) < ans) {
                ans = sum(check1, k + 1);
            }
        }
    }
    printf("%d\n", (ans != MAX_SIZE) ? ans : 0);
}

int sum(int arr[], int size) {
    int i, total = 0;
    for (i = 0; i < size; i++) {
        total += arr[i];
    }
    return total;
}

int main() {
    int n, k, i;
    scanf("%d %d", &n, &k);
    for (i = 0; i < n; i++) {
        int x;
        scanf("%d", &x);
        rainbow[i] = x;
        check2[x] += 1;
    }

    dp(n, k);

    return 0;
}


/*
알고리즘:
	투포인터를 이용해 문제를 풀이했다.
	check1은 P'의 원소들을 체크하는 배열이고,
	check2는 P-P'의 원소들을 체크하는 배열이다.
	s와 e는 각각 P'의 시작과 끝을 가리키는 포인터이다.
	s와 e는 초기값이 0이므로 check1 배열은 모두 0으로,
	check2 배열은 각 값에 맞는 P의 원소의 개수로 초기화한다.

	dp() 함수에서 s와 e를 이용해 P'의 원소들을 체크한다.
	먼저 e를 움직이며 P'의 원소들을 체크한다.
	만약 s가 가리키는 원소와 e가 가리키는 원소가 같다면
	굳이 같은 값을 가지고 있을 필요가 없으므로
	s를 한 칸 오른쪽으로 옮겨 기존의 s값을 P-P'에 포함시켜
	P'와 P-P' 두 집합 모두가 기존의 s값을 가질 수 있도록 한다.
	이 과정이 한 번 끝나면 check1과 check2를 인덱스 1의 값부터 확인해 0이 있는지 확인한다.
	만약 0이 없다면 P'와 P-P' 두 집합 모두가 모든 원소를 가지고 있다는 의미이므로
	ans 값과 비교하여 더 작은 값을 ans에 저장한다.

수행시간:
	n만큼 반복하는 반복문 내부에서 k만큼 반복하는 반복문이 있으므로
	시간복잡도는 O(nk)이다.
*/
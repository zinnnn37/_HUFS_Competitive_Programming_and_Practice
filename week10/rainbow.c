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

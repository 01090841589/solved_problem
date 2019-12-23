#include <stdio.h>
#define MAX 200008

int T, N, res;
int arr[MAX], updown[MAX];
int left, right, comp, mid;


int findupdown(int k) {
	int n = (N + 1) / 2;
	for (int i = 1; i < N + 1; i++) {
		updown[i] = arr[i] >= k ? 1 : 0;
	}
	for (int p = n - 1, q = n + 1; p >= 1; p--, q++) {
		if (updown[p] == updown[p + 1]) return updown[p];
		if (updown[q] == updown[q - 1]) return updown[q];
	}
	if (n % 2 == 0) return 1 - updown[n];
	return updown[n];
}

int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		N = N * 2 - 1;
		for (int i = 1; i < N+1; i++) {
			scanf(" %d", &arr[i]);
		}
		left = 1;
		right = N;
		res = 0;
		while (left <= right) {
			mid = (left + right) / 2;
			if (findupdown(mid)) {
				res = mid < res ? res : mid;
				left = mid + 1;
			}
			else right = mid - 1;
		}
		printf("#%d %d\n", tc+1, res);



	}


	return 0;
}
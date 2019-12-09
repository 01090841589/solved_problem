#include <stdio.h>

int T, N;
int arr[200002];
int now, result, sums;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		result = -9999;
		now = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
		}
		for (int i = 0; i < N; i++) {
			
			if (arr[i] < now + arr[i]) {
				now = now + arr[i];
			}
			else {
				now = arr[i];
			}

			if (result < now) {
				result = now;
			}
		}
		printf("#%d %d\n", tc + 1, result);
	}

	return 0;
}
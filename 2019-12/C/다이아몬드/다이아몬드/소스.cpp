#include <stdio.h>

int T, N, K, n;
int scr, res;
int main() {
	freopen("Text.txt", "r", stdin);

	scanf(" %d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf(" %d %d", &N, &K);
		int arr[10000] = { 0, };
		res = 0;
		for (int i = 0; i < N; i++) {
			scanf(" %d", &n);
			arr[n]++;
		}
		for (int i = 0; i < 10000 - K; i++) {
			scr = 0;
			if (arr[i] > 0) {
				for (int j = i; j < i + K + 1; j++) {
					scr += arr[j];
				}
				if (res < scr) {
					res = scr;
				}
			}
		}
		printf("#%d %d\n", tc + 1, res);
	}
	return 0;
}
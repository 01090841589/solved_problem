#include <stdio.h>

int T, N, K;
int arr[200002];
int S[200002];
int low, mid, high, flag, len;

int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d %d", &N, &K);
		low = 200000;
		high = 0;
		len = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &arr[i]);
			if (arr[i] > high) {
				high = arr[i];
			}
			if (arr[i] < low) {
				low = arr[i];
			}
		}
		for (int i = 0; i < K; i++) {
			scanf("%d", &S[i]);
			len += S[i];
		}
		while (low < high) {
			mid = (low + high) / 2;
			flag = 1;

			int scr = 0;
			int sums = len;
			for (int i = 0; i < K; i++) {
				if (sums > N - scr) {
					flag = 0;
					break;
				}
				int flag2 = 1;
				while (flag2) {
					flag2 = 0;
					for (int j = 0; j < S[i]; j++) {
						if (scr >= N) {
							flag = 0;
							break;
						}
						if (arr[scr] > mid) {
							flag2 = 1;
							scr++;
							break;
						}
						scr++;
					}
				}
				sums -= S[i];
			}

			if (flag) {
				high = mid;
			}
			else {
				low = mid + 1;
			}
			mid = (low + high) / 2;


		}
		printf("#%d %d\n", tc + 1, mid);

	}

	return 0;
}
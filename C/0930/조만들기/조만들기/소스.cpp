#include <stdio.h>

int T;
int N, K;
int j, result;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		scanf("%d", &K);
		j = 0;
		result = 0;
		for (int i = 0; i < N; i++) {
			if (i % 2 == 0) {
				j++;
				result += j;
			}
			else if (i % 2 == 1) {
				j += (2 * K) - 1;
				result += j;
			}

		}

		printf("#%d ", tc + 1);
		for (int i = 0; i < K; i++) {

			printf("%d ", result);
			if (N % 2 == 1) {
				result++;
			}
		}
		printf("\n");
	}



	return 0;
}
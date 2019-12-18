#include <stdio.h>

int T;
int N, D;
int gate[300000];
int already[300000];
int idx;
int result;
int K;
int main() {

	freopen("ºÎ¸Ô¿Õ±¹.txt", "r", stdin);
	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		scanf("%d", &D);
		idx = 0;
		result = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &gate[i]);
			if (gate[i] == 1) {
				already[idx] = i;
				idx++;

			}
		}
		for (int i = 0; i < idx; i++) {
			if (i == 0) {
				if (already[i] + 1 > D) {
					result += already[i] / D;
					if (already[i] % D > 0) {
						result++;
					}
				}

			}
			else {
				K = already[i] - already[i - 1] -D;

				result += K / D;
				if (K%D > 0) {
					result++;
				}

			}
		}
		if (idx == 0) {
			result += N / D;
			if (N % D > 0) {
				result += 1;
			}

		}




		printf("#%d %d\n", tc + 1, result);
	}
	return 0;
}
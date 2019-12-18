#include <stdio.h>


int T;
int j;
int N;
int cnt;
int main() {
	freopen("상원이의연속합.txt", "r", stdin);
	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		cnt = 0;
		for (int i = 1; i < N; i++) {
			j = 0;
			for (int k = i; j < N; k++) {
				j += k;

			}
			if (j == N) {
				cnt += 1;
			}
		}



		printf("#%d %d\n", tc + 1, cnt+1);
	}
	return 0;
}
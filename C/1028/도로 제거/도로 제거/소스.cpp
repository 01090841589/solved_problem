#include <stdio.h>

int T;
int M, N;
int a, b;
int cnt;
int scr;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		scanf("%d", &M);
		cnt = (N * (N - 1)) / 2;
		scr = N - 1;
		for (int i = 0; i < M; i++) {
			cnt -= 1;
			scanf("%d", &a);
			scanf("%d", &b);

		}


		printf("#%d %d\n", tc + 1, (cnt - scr));
	}
	return 0;
}
#include <stdio.h>

int T;
int N, M;
int score[20][20];
int high;
int many;
int cnt;
int main() {
	freopen("동철이의프로그래밍대회.txt", "r", stdin);
	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		scanf("%d", &M);
		high = 0;
		many = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				scanf("%d", &score[i][j]);
			}
		}
		for (int i = 0; i < N; i++) {
			cnt = 0;
			for (int j = 0; j < M; j++) {
				if (score[i][j]) {
					cnt += 1;
				}
			}
			if (high == cnt) {
				many += 1;
			}
			if (high < cnt) {
				high = cnt;
				many = 1;
			}
		}





		printf("#%d %d %d\n", tc + 1, many, high);
	}


	return 0;
}
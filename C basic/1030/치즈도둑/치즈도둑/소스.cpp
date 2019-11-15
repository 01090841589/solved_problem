#include <stdio.h>

int T, N;
int MAP[101][101];
int visit[101][101];
int result, cnt;
int diry[4] = { 1, 0, -1, 0 };
int dirx[4] = { 0, 1, 0, -1 };
int findcheese(int y, int x ,int k) {
	int Y, X;
	for (int i = 0; i < 4; i++) {
		Y = y + diry[i];
		X = x + dirx[i];
		if (0 <= X && X < N && 0 <= Y && Y <= N) {
			if (MAP[Y][X] > 0 && visit[Y][X] < k) {
				visit[Y][X] = k;
				findcheese(Y, X, k);
			}

		}
	}
	return 0;
}

int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				scanf("%d", &MAP[i][j]);
				visit[i][j] = 0;
			}
		}
		result = 1;
		for (int k = 1; k < 101; k++) {
			cnt = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (MAP[i][j] == k) {
						MAP[i][j] = 0;
					}
				}
			}
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (MAP[i][j] > k-1 && visit[i][j] < k) {
						visit[i][j] = k;
						cnt += 1;
						findcheese(i, j, k);
					}
				}
			}
			if (result < cnt) {
				result = cnt;
			}


		}





		printf("#%d %d\n", tc + 1, result);
	}
	return 0;
}
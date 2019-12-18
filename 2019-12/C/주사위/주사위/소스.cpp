#include <stdio.h>

int T, N, M;
int result;
int DIR[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
int DICE[6][4] = { {5, 2, 3, 4}, {3, 4, 5, 2}, {2, 1, 2, 0}, {0, 3, 1, 3}, {4, 0, 4, 1}, {1, 5, 0, 5} };
int xst, yst;
int MAP[8][8];
int visited[8][8];

void dice(int y, int x, int k, int status) {
	if (k >= result) return;
	if (MAP[y][x] == 3) {
		if (result > k && status == 0) {
			result = k;
		}
		return;
	}
	for (int c = 0; c < 4; c++) {
		int Y = y + DIR[c][0];
		int X = x + DIR[c][1];
		if (0 <= Y && Y < N && 0 <= X && X < M && MAP[Y][X]) {
			if (visited[Y][X] == 0) {
				visited[Y][X] = 1;
				dice(Y, X, k + 1, DICE[status][c]);
				visited[Y][X] = 0;
			}
		}
	}
}



int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf(" %d %d", &N, &M);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				scanf("%d", &MAP[i][j]);
				if (MAP[i][j] == 2) {
					yst = i;
					xst = j;
				}
				visited[i][j] = 0;
			}
		}
		result = 100;
		visited[yst][xst] = 1;
		dice(yst, xst, 0, 0);
		if (result == 100) {
			result = -1;
		}
		printf("#%d %d\n", tc + 1, result);

	}

	return 0;
}
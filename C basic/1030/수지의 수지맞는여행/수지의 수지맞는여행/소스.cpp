#include <stdio.h>

int T, R, C;
char size[21][21];
int MAP[21][21];
int visited[21][21];
int visit[27];
int result, scr;
int dirx[4] = { 0, 0, 1, -1 };
int diry[4] = { 1, -1, 0, 0 };

int trip(int y, int x, int k) {
	int Y, X;
	for (int i = 0; i < 4; i++) {
		Y = y + diry[i];
		X = x + dirx[i];
		if (0 <= Y && Y < R && 0 <= X && X < C) {
			if (visit[MAP[Y][X]] == 0) {
				visit[MAP[Y][X]] = 1;
				trip(Y, X, k + 1);
				visit[MAP[Y][X]] = 0;
			}
		}
	}
	scr = 0;
	for (int i = 0; i < 26; i++) {
		if (visit[i] == 1) {
			scr += 1;
		}
	}
	if (result < scr) {
		result = scr;
	}

	return 0;
}

int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d %d", &R, &C);
		result = 0;
		for (int i = 0; i < R; i++) {
			scanf("%s", &size[i]);
		}

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				MAP[i][j] = size[i][j]-65;
				visited[i][j] = 0;
			}
		}
		for (int i = 0; i < 27; i++) {
			visit[i] = 0;
		}

		visited[0][0] = 1;
		visit[MAP[0][0]] = 1;

		trip(0, 0, 1);

		printf("#%d %d\n", tc + 1, result);
	}
	return 0;
}
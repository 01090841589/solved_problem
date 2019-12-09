#include <stdio.h>
#include <vector>
int N, M, T;
int MAP[51][51];
int x, d, k;

int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d %d %d", &N, &M, &T);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &MAP[i][j]);
		}
	}
	for (int i = 0; i < T; i++) {
		scanf("%d %d %d", &x, &d, &k);
		printf("%d %d %d", x, d, k);

	}
	return 0;
}
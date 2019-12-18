#include <stdio.h>


int T, N, K;
int x[502];
int y[502];
int len[501];
int buf;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf(" %d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf(" %d %d", &N, &K);
		for (int i = 0; i < N; i++) {
			scanf(" %d %d", &x[i], &y[i]);

		}
	}

	return 0;
}
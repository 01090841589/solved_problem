#include <stdio.h>

int T;
int N, K;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d %d", &N, &K);
		if (K <= 1 || K >= (N * 2 - 1)) {
			printf("#%d 0\n", tc+1);
		}
		else {
			printf("#%d 1\n", tc + 1);
		}
	}
	return 0;
}
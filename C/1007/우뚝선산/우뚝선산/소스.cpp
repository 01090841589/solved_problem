#include <stdio.h>

int T, N;
int mount[50001];
int up, down;
int result;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%d", &mount[i]);
		}
		up = 0;
		down = 0;
		result = 0;
		for (int i = 1; i < N; i++) {
			if (mount[i - 1] < mount[i] && down == 0) {
				up++;
			}
			else if (mount[i - 1] > mount[i] && up > 0) {
				down++;
			}
			else {
				result += up * down;
				up = 0;
				down = 0;
				if (mount[i - 1] < mount[i]) {
					up = 1;
				}
			}
		}
		if (up > 0 && down > 0) {
			result += up * down;
		}

		printf("#%d %d",tc + 1, result);
	}




	return 0;
}
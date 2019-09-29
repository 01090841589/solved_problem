#include <stdio.h>

int T;
int S, E, M;
int result, buf;

int main() {
	freopen("sem.txt", "r", stdin);
	scanf("%d", &T);
	// 365, 24, 29
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &S);
		scanf("%d", &E);
		scanf("%d", &M);
		result = 0;
		while (S + E + M > 0) {
			buf = S;
			if (E > buf) {
				buf = E;
			}
			if (M > buf) {
				buf = M;
			}

			S -= buf;
			while (S < 0) {
				S += 365;
			}
			E -= buf;
			while (E < 0) {
				E += 24;
			}
			M -= buf;
			while (M < 0) {
				M += 29;
			}

			result += buf;
		}
		printf("#%d %d\n", tc + 1, result);
	}
	return 0;
}

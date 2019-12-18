#include <stdio.h>


int T;
int N;
long long A, B;
long long result;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d %d %d", &N, &A, &B);
		if (N > 1) {
			result = (B*(N - 2)) - (A*(N - 2)) + 1;
			if (result >= 0) {
				printf("#%d %lld\n", tc + 1, result);
			}
			else {
				printf("#%d 0\n", tc + 1);
			}
		}
		else if (N == 1) {
			if (A == B) {
				printf("#%d 1\n", tc + 1);
			}
			else {
				printf("#%d 0\n", tc + 1);
			}
		}
		else {
			printf("#%d 0\n", tc+1);
		}
	}
	return 0;
}
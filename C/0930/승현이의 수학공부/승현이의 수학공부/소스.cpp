#include <stdio.h>

int T;
int N, Y;
int result;
int K, ten;
int flag;
char X;
int main() {
	freopen("수학공부.txt", "r", stdin);

	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		flag = 1;
		while (flag) {
			scanf("%c", &X);
			if (X == 10) {
				break;
			}
			printf("%d ", X);

		}
		ten = 1;
		Y = 0;
		while (X > 0) {
			K = X % 10;
			Y += K * ten;
			X = X / 10;
			ten = ten * N;
		}
		result = Y % (N-1);
		printf("#%d %d\n", tc+1, result);
	}
	return 0;
}
#include <stdio.h>



int T, K;
long long A, B;
long long buf;

int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &K);
		A = 2;
		B = 1;
		for (int a = 1; a < K; a++) {
			buf = A;
			A = A + B;
			B = buf;
		}
		printf("#%d %lld %lld\n", tc + 1, A, B);




	}




	return 0;
}
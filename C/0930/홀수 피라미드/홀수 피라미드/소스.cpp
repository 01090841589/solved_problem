#include <stdio.h>


int T;
long long N;
long long a, b;
int main() {
	freopen("피라미드.txt", "r", stdin);

	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		b = (N*N)*2 - 1;
		a = ((N-1)*(N-1))*2 + 1;
		if (N == 1) {
			a = 1;
		}



		printf("#%d %lld %lld\n", tc + 1,a, b);
	}

	return 0;
}
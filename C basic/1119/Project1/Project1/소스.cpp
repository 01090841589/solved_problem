#include <stdio.h>

int T;
long long N, result;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		result = 0;
		scanf("%lld", &N);
		result = ((N - 1) / 2)*((N - 1) / 2);
		printf("#%d %lld\n", tc+1, result);
	}
	return 0;
}`
#include <stdio.h>


int T, N;
long long arr[1001];
long long k, a;

long long facto(long long n) {
	if (n == 0){
	return 0;
	}
	a = 1;
	for (long long j = n; j > 1; j--) {
		a *= j;
		a = a % 1000000007;
	}
	return a;
}

int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (long long i = 2; i < 1001; i++) {
		k = i * arr[i - 1] + (i / 2) * facto(i - 1);
		arr[i] = k % 1000000007;
	}
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);




		printf("#%d %lld\n", tc + 1, arr[N]);
	}
	return 0;
}
#include <stdio.h>

int T;
long long K;
int result;
int main() {
	freopen("자가복제문자열.txt", "r", stdin);

	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%lld", &K);
		while (true) {
			if (K % 4 == 3) {
				result = 1;
				break;
			}
			if (K % 4 == 1) {
				result = 0;
				break;
			}
			if (K % 8 == 6) {
				result = 1;
				break;
			}
			if (K % 8 == 2) {
				result = 0;
				break;
			}
			if (K % 4 == 0) {
				K = K / 4;
			}
		}
		printf("#%d %d\n",tc+1, result);
	}
	return 0;
}
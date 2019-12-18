#include <stdio.h>

int T;
int s, t, a, b;
int result;

int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		result = 0;
		scanf("%d", &s);
		scanf("%d", &t);
		scanf("%d", &a);
		scanf("%d", &b);
		while (s < t) {
			if (t-s)
			if (b <= 1) {
				break;
			}
			if (t % b == 0 && t/b >= s) {
				t = t / b;
				result += 1;
			}
 			else {
				break;
			}
		}
		if ((t-s) % a != 0) {
			result = -1;
		}
		else {
			result += (t - s) / a;
		}


		printf("#%d %d\n", tc + 1, result);
	}
	return 0;
}
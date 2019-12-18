#include <stdio.h>

int T;
char c[100];
int n, w, cnt;
int result_up, result_down;
double angle;
double buf;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		for (int i = 0; i < 100; i++) {
			c[i] = 0;
		}
		scanf("%s", &c);
		n = 0;
		w = 0;
		cnt = 0;
		angle = 0;
		for (int i = 0; i < 100; i++) {
			if (c[i] == 0) {
				break;
			}
			if (c[i] == 'n') {
				n += 1;
				cnt += 1;
				buf = 90;
				for (int j = 1; j < cnt; j++) {
					buf /= 2;
				}
				angle -= buf;
				if (angle < 0) {
					angle = 0;
				}

			}
			else if (c[i] == 'w') {
				w += 1;
				cnt += 1;
				buf = 90;
				for (int j = 1; j < cnt; j++) {
					buf /= 2;
				}
				angle += buf;
				if (angle > 90) {
					angle = 90;
				}

			}
		}
		result_down = 1;
		result_up = 0;
		printf("%.20f ", angle);
		while (result_down > 0) {
			result_up = angle;
			if (angle - result_up > 0) {
				angle *= 2;
				result_down *= 2;
			}
			else {
				break;
			}
		}
		result_up = angle;
		if (result_down < 2) {
			printf("#%d %d\n", tc + 1, result_up);
		}
		else {
			printf("#%d %d/%d\n", tc + 1, result_up, result_down);
		}
	}
	return 0;
}

// west north
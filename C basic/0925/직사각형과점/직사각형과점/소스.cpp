#include <stdio.h>
int xy[4];
int dot[20000];
int N;
int cnt;
int dots[3];
int main() {
	int T;
	freopen("직사각형과점.txt", "r", stdin);

	scanf("%d", &T);

	for (int tc =0; tc < T; tc++) {
		for (int i = 0; i < 4;  i++) {
			scanf("%d", &xy[i]);
		}
		scanf("%d", &N);
		for (int i = 0; i < (N*2); i++) {
			scanf("%d", &dot[i]);
		}


		for (int i = 0; i < 3; i++) {
			dots[i] = 0;
		}

		for (int i = 0; i < N; i++) {
			cnt = 0;
			if (xy[0] <= dot[i * 2] && dot[i * 2] <= xy[2]) {
				cnt += 1;
			}
			if (xy[1] <= dot[i * 2 + 1] && dot[i * 2 + 1] <= xy[3]) {
				cnt += 1;
			}
			if (cnt == 0 || cnt == 1) {
				dots[2] += 1;
			}
			else if (cnt == 2) {
				cnt = 0;
				if (dot[i * 2] == xy[0] || dot[i * 2] == xy[2]) {
					cnt += 1;
				}
				if (dot[i * 2+1] == xy[1] || dot[i * 2+1] == xy[3]) {
					cnt += 1;
				}
				if (cnt == 0) {
					dots[0] += 1;
				}
				else if (cnt > 0) {
					dots[1] += 1;
				}
			}
		}




		printf("#%d %d %d %d\n", tc+1, dots[0], dots[1], dots[2]);
	}
	return 0;
}
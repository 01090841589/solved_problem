#include <stdio.h>

int T;
char X[100];
int arr[100];
int cnt;
int main() {
	freopen("다양성측정.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; ++tc) {
		cnt = 0;
		for (int i = 0; i < 20; i++) {
			arr[i] = 0;
			X[i] = 0;
		}
		scanf(" %s", &X);
		for (int i = 0; i < 20; i++) {
			arr[X[i] - 48] += 1;



		}

		for (int i = 0; i < 20; i++) {
			if (arr[i] > 0) {
				cnt += 1;
			}
		}
		printf("#%d %d\n", tc+1, cnt);


	}

}
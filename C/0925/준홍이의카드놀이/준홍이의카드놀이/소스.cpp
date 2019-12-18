#include <stdio.h>


int T;
int N;
int M;
int NUM[41];
int win;
int main() {
	freopen("ÁØÈ«ÀÌÀÇÄ«µå³îÀÌ.txt", "r", stdin);
	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		scanf("%d", &M);
		win = 0;
		for (int i = 0; i < 41; i++)
			NUM[i] = 0;

		for (int i = 1; i < N; i++) {
			for (int j = 1; j < M; j++) {
				NUM[i + j] += 1;
				if (win < NUM[i + j]){
					win = NUM[i + j];
				}


			}

		}
		printf("#%d ", tc + 1);

		for (int i = 0; i < 41; i++) {
			if (NUM[i] == win) {
				printf("%d ", i+1);
			}
		}
		printf("\n");
	}





	return 0;
}
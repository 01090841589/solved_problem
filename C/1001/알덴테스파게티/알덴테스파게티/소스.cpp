#include <stdio.h>

int T;
int N, B, E;
int time[10000];
int mint, maxt;
int result;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		scanf("%d", &B);
		scanf("%d", &E);	
		result = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &time[i]);
			mint = (B/time[i])*time[i];
			maxt = (B/time[i])*time[i]+time[i];

			if (mint + E >= B || maxt - E <= B) {
				result += 1;
			}

		}
		printf("#%d %d\n", tc+1, result);

	}

	return 0;
}
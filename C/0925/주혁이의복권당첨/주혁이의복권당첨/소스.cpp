#include <stdio.h>
int N;
int M;
char lotto[100][8];
char buy_lotto[1000][8];
int prize[1000];
long long result;
int flag;
int cnt;
int main() {
	freopen("¡÷«ı¿Ã¿«∫π±«¥Á√∑.txt", "r", stdin);

	int T;
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		scanf("%d", &M);
		result = 0;
		for (int i = 0; i < N; i++) {
			scanf(" %s", &lotto[i]);
			scanf("%d", &prize[i]);
		}
		for (int i = 0; i < M; i++) {
			scanf(" %s ", &buy_lotto[i]);
		}
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				flag = 0;
				cnt = 0;
				for (int k = 0; k < 8; k++) {
					if (lotto[j][k] == '*') {
						cnt += 1;
						continue;
					}
					if (buy_lotto[i][k] == lotto[j][k]) {
						cnt += 1;
					}
					if (cnt == 8) {
						result += prize[j];
						flag = 1;
					}
				}
				if (flag) {
					break;
				}
			}
		}




		printf("#%d %lld\n", tc+1, result);
	}
	return 0;
}
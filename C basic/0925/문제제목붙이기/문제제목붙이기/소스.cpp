#include <stdio.h>

int T;
int N;
int result;
char alpha;
char words[100][30];
int main() {
	setbuf(stdout, NULL);
	
	freopen("문제제목붙이기.txt", "r", stdin);
	scanf("%d", &T);
	result = 0;
	for (int tc = 0; tc < T; tc++) {
		alpha = 'a';
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf(" %s", &words[i]);

		}
		int k = 0;
		while (k != alpha) {
			k = alpha;
			for (int i = 0; i < N; i++) {
				if (words[i][0] == alpha || words[i][0] == alpha - 32) {
					alpha = 1 + alpha;
					break;
				}
			}
		}
		printf("#%d %d\n", tc + 1,alpha-97);

	}


	return 0;
}
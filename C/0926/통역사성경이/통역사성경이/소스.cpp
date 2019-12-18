#include <stdio.h>

int T;
int N;
int M;
int cnt;
int flag;
char word[100];
int main() {
	freopen("통역사성경이.txt", "r", stdin);

	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		M = 0;
		cnt = 0;
		printf("#%d ", tc+1);
		while (M < N) {
			flag = 1;
			scanf(" %s", &word);
			for (int i = 0; i < 100; i++) {
				if (i == 0) {
					if (word[i] < 65 || word[i]>90) {
						flag = 0;
					}
				}
				if (word[i] == 0) {
					if (flag == 1) {
						cnt++;
					}
					break;
				}
				if (word[i] == '!') {
					if (flag) {
						cnt++;
					}
					printf("%d ", cnt);
					M++;
					cnt = 0;
					break;
				}
				if (word[i] == '?') {
					if (flag) {
						cnt++;
					}
					printf("%d ", cnt);
					M++;
					cnt = 0;
					break;
				}
				if (word[i] == '.') {
					if (flag) {
						cnt++;
					}
					printf("%d ", cnt);
					M++;
					cnt = 0;
					break;
				}
				if (i > 0) {
					if (word[i] < 97 || word[i]>122) {
						flag = 0;
					}
				}
			}
			
		}
		printf("\n");
		
	}
	return 0;
}
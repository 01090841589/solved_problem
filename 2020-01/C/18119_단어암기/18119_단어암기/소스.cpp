#include <stdio.h>

int N, M, comm, spell, res;
char word[1005];
int alpabet[10005][28];

int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf("%s", &word);
		for (int j = 0; j < 1001; j++) {
			if (word[j] == 0) {
				alpabet[i][0] = j - 1;
				alpabet[i][1] = j - 1;
				break;
			}
			alpabet[i][word[j] - 95] = 1;
		}
	}
	for (int i = 0; i < M; i++) {
		scanf("%d %s", &comm, &spell);
		spell -= 95;
		res = 0;
		if (comm == 1) {
			for (int j = 0; j < N; j++) {
				if (alpabet[j][spell] == 1){
					alpabet[j][spell] = -1;
					alpabet[j][1] -= 1;
				}
				if (alpabet[j][0] == alpabet[j][1]) {
					res++;
				}
			}
			printf("%d\n", res);
		}
		else {
			for (int j = 0; j < N; j++) {
				if (alpabet[j][spell] == -1) {
					alpabet[j][spell] = 1;
					alpabet[j][1] += 1;
				}
				if (alpabet[j][0] == alpabet[j][1]) {
					res++;
				}
			}
			printf("%d\n", res);
		}
	}
	return 0;
}
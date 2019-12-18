#include <stdio.h>
char N[20][100][100];
int W;
int K;
int leng[100];
int main() {
	freopen("Text.txt", "r", stdin);

	scanf("%d", &W);
	scanf("%d", &K);

	for (int i = 0; i < W; i++) {
		for (int j = 0; j < W; j++) {
			scanf(" %s", &N[i][j]);
		}

	}

	for (int i = 0; i < W; i++) {
		for (int j = 0; j < W; j++) {
			printf("%s ", N[i][j]);
		}
		printf("\n");

	}


	return 0;
}

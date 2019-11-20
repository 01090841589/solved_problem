#include <stdio.h>

int T;
int A, B, C, D, E;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d %d", &A, &B);
		if (A % 2 == 1) {
			A++;
		}
		if (A < (B * 2)) {
			printf("No DAP!\n");
		}
		else {
			C = A - 1;
			D = 0;
			E = 0;
			for (int i = 0; i < A; i++) {
				if (i < B || i >= A - B) {
					for (int j = 0; j < A * 2; j++) {
						if (j > C-1 && j < (A * 2 - C-1)) {
							printf("*");
						}
						else if (j < C) {
							printf(" ");
						}
					}
				}
				else {
					D++;
					for (int j = 0; j < A * 2; j++) {
						if (j > C-1 && j < (A * 2 - C-1)) {
							if (j > A-D-1 && j < A+D-1) {
								printf("+");

							}
							else {
								printf("*");

							}
						}
						else if (j < C) {
							printf(" ");
						}
					}
				}
				C--;
				printf("\n");
			}
		}
	}

	return 0;
}

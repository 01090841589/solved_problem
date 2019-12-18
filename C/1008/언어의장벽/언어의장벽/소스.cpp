#include <stdio.h>

int T;
int A, B;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d %d", &A, &B);
		if (A < (B * 2)) {
			printf("No DAP\n");
		}
		else {
			for (int i = 0; i < A+(1-(A%2)); i++) {
				for (int j = 0; j < A+ (1-(A % 2)); j++) {

					if (i < B || i >(A - (A % 2) - B)){

						if (j < A / 2 + (1 - (A % 2))) {
							printf("%c", 65 + j);
						}
						else {
							printf("%c", 65 + A - j - (A % 2));
						}
					
					}
					else {
						if (j < B || j >(A - (A % 2) - B)) {

							if (j < A / 2 + (1 - (A % 2))) {
								printf("%c", 65 + j);
							}
							else {
								printf("%c", 65 + A - j - (A % 2));
							}
						}
						else {
							printf("+");
						}
					}


				}
				printf("\n");
			}
		}
				printf("\n");
	}

	return 0;
}
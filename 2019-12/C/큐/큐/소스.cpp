#include <stdio.h>

int T;
int queue[10000];
int front, back, num;
char com[10];
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	back = 0;
	front = 0;
	for (int tc = 0; tc < T; tc++) {
		scanf("%s", &com);
		if (com[1] == 'u') {
			scanf("%d", &num);
			queue[back] = num;
			back++;
		}
		else if (com[1] == 'o') {
			if (back-front > 0) {
				printf("%d\n", queue[front]);
				front++;
			}
			else {
				printf("-1\n");
			}
		}
		else if (com[1] == 'i') {
			printf("%d\n", back - front);
		}
		else if (com[1] == 'm') {
			if (back - front > 0) {
				printf("0\n");
			}
			else {
				printf("1\n");
			}

		}
		else if (com[1] == 'r') {
			if (back - front > 0) {
				printf("%d\n", queue[front]);
			}
			else {
				printf("-1\n");
			}

		}
		else if (com[1] == 'a') {
			if (back - front > 0) {
				printf("%d\n", queue[back-1]);
			}
			else {
				printf("-1\n");
			}

		}

	}

	return 0;
}
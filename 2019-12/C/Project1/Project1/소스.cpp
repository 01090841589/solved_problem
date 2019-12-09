#include <stdio.h>

int T, num, cnt;
char *com[10];
int stack[10000];
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	cnt = 0;
	for (int tc = 0; tc < T; tc++) {
		scanf("%s", &com);
		if (com[1] == 'u') { //push
			scanf("%d", &num);
			stack[cnt] = num;
			cnt++;
		}
		else if (com[0] == 't') { // top
			if (cnt > 0) {
				printf("%d\n", stack[cnt - 1]);
			}
			else {
				printf("-1\n");
			}
		}
		else if (com[0] == 's') { // size
			printf("%d\n", cnt);
		}
		else if (com[0] == 'e') { // empty
			if (cnt > 0) {
				printf("0\n");
			}
			else {
				printf("1\n");
			}
		}
		else { // pop
			if (cnt > 0) {
				printf("%d\n", stack[cnt - 1]);
				cnt--;
			}
			else {
				printf("-1\n");
			}
		}
	}
	return 0;
}
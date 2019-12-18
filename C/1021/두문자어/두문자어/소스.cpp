#include <stdio.h>

int T;
char a[100], b[100], c[100];
int main(){
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf(" %s", &a);
		scanf(" %s", &b);
		scanf(" %s", &c);

		a[0] = a[0] - 32;
		b[0] = b[0] - 32;
		c[0] = c[0] - 32;
		printf("#%d %c%c%c\n", tc+1, a[0], b[0], c[0]);
	}
	return 0;
}
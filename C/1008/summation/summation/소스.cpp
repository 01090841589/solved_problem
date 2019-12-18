#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int T;
int N[10];
int result;
int res[10];
int buf;

int compare(const void * a, const void * b)
{
	return (*(int*)b - *(int*)a);
}
int compare2(const void * a, const void * b)
{
	return (*(int*)a - *(int*)b);
}
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		for (int i = 0; i < 10; i++) {
			scanf("%d", &N[i]);
			buf = 0;
			while (N[i] > 0) {
				buf += N[i] % 10;
				N[i] = N[i] / 10;
			}
			res[i] = buf;
		}
		qsort(res, 10, sizeof(int), compare);

		printf("#%d %d %d\n", tc + 1, res[0], res[9]);
	}
	return 0;
}
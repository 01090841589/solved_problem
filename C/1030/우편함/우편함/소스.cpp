#include <stdio.h>


int T, N, A, B;
int time;
int letter[101];
int stack[101];
int letters;
int result[101];
int results;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		time = 0;
		scanf("%d %d %d", &N, &A, &B);
		letters = 0;
		results = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &letter[i]);
			result[i] = 0;
		}
		for (int i = 0; i < 2001; i++) {
			if (i == letter[time]) {
				stack[letters] = letter[time];
				letters++;
				time++;
			}
			if (letters == A) {
				for (int j = 0; j < (letters / 2+(letters%2)); j++) {
					result[results] = i;
					results++;
				}
				for (int j = (letters / 2 + (letters % 2)); j < letters; j++) {
					stack[j - (letters / 2 + (letters % 2))] = stack[j];
					stack[j] = 0;
				}
				letters -= letters / 2 + (letters % 2);
			}
			else if (stack[0]+B == i) {
				if (stack[1] == 0 && i >= letter[N-1]) {
					result[results] = i;
					stack[0] = 0;
					break;
				}
				for (int j = 0; j < (letters / 2 + (letters % 2)); j++) {
					result[results] = i;
					results++;
				}
				for (int j = (letters / 2 + (letters % 2)); j < letters; j++) {
					stack[j - (letters / 2 + (letters % 2))] = stack[j];
					stack[j] = 0;
				}
				letters -= letters / 2 + (letters % 2);

			}
		}

		printf("#%d ", tc + 1);
		for (int i = 0; i < N; i++) {
			printf("%d ", result[i]);
		}
		printf("\n");
	}
	return 0;
}
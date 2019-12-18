#include <stdio.h>


int T;
char word1[12];
char word2[12];
int left, right;
int leftlen, rightlen;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		scanf(" %s", &word1);
		scanf(" %s", &word2);
		left = 0;
		right = 0;
		for (int i = 0; i < 12; i++) {
			if (word1[i] == 0 || word2[i] == 0) {
				if (word1[i] == 0 && word2[i] == 0) {
					break;
				}
				left = 0;
				right = 1;
				break;
			}
			if (word1[i] == 'B') {
				left += 2;
			}
			else if (word1[i] == 'A') {
				left++;
			}
			else if (word1[i] == 'D') {
				left++;
			}
			else if (word1[i] == 'O') {
				left++;
			}
			else if (word1[i] == 'P') {
				left++;
			}
			else if (word1[i] == 'Q') {
				left++;
			}
			else if (word1[i] == 'R') {
				left++;
			}
			// 65 68 79 80 81 82 66
			if (word2[i] == 'B') {
				right += 2;
			}
			else if (word2[i] == 'A') {
				right++;
			}
			else if (word2[i] == 'D') {
				right++;
			}
			else if (word2[i] == 'O') {
				right++;
			}
			else if (word2[i] == 'P') {
				right++;
			}
			else if (word2[i] == 'Q') {
				right++;
			}
			else if (word2[i] == 'R') {
				right++;
			}
			// 65 68 79 80 81 82 66

			if (left != right) {
				break;
			}
		}
		if (left == right) {
			printf("#%d SAME\n", tc+1);
		}
		else if (left != right){
			printf("#%d DIFF\n", tc+1);
		}
	}

	return 0;
}
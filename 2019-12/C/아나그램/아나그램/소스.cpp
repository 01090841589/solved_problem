#include <stdio.h>

int T;
char s1[100002], s2[100002];
int sort1[27], sort2[27];
int len, result, flag;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%s %s", &s1, &s2);
		for (int i = 0; i < 26; i++) {
			sort1[i] = 0;
			sort2[i] = 0;
		}
		len = 0;
		result = 0;
		for (int i = 0; i < 100000; i++) {
			if (s1[i] == 0) {
				break;
			}
			sort1[s1[i] - 'a']++;
			len++;
		}
		for (int i = 0; i < 100000; i++) {
			if (s2[i] == 0) {
				break;
			}
			if (i < len - 1) {
				sort2[s2[i] - 'a'] ++;
			}
			else {
				sort2[s2[i] - 'a'] ++;
				sort2[(s2[i-len]) - 'a'] --;
			}

			if (i >= len-1) {
				flag = 1;
				for (int j = 0; j < 26; j++) {
					if (sort1[j] != sort2[j]) {
						flag = 0;
						break;
					}
				}
				if (flag) {
					result++;
				}


			}
		}
		printf("#%d %d\n", tc+1, result);
	}
	return 0;
}
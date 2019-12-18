#include <stdio.h>

int T;
int N, M;
int alpa[26];
long long result;
int main() {
	freopen("ø¿≈∏.txt", "r", stdin);
	scanf("%d", &T);
	printf("%d\n", 'a');
	for (int tc = 0; tc < T; tc++) {
		char word[1000];
		N = 0;
		M = 0;
		scanf(" %s", &word);
		printf("%s", word);
		result = 1;

		for (int i = 0; i < 26; i++) {
			alpa[i] = 0;
		}
		for (int i = 0; i < 1000; i++) {
			if (word[i] == 0) {
				break;
			}
			alpa[word[i] - 'a'] += 1;
		}

		for (int i = 0; i < 26; i++) {
			if (alpa[i] > 0) {
				N += alpa[i];
				M += 1;
			}
		}
		for (int i = N; i > (N-M); i--) {
			
			result *= i;

		}
		printf("%d %d %d\n", N,M, result);
	}

	return 0;
}
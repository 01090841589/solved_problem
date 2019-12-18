#include <stdio.h>

int T;
int N, M, buf;
int opt[4];
int nums[13];
int calcul[13];
int sums;
int low, high;
int idx;
int operation() {
	buf = nums[0];
	for (int b = 0; b < M; b++) {
		if (calcul[b] == 0) {
			buf += nums[b + 1];
		}
		else if (calcul[b] == 1) {
			buf -= nums[b + 1];
		}
		else if (calcul[b] == 2) {
			buf *= nums[b + 1];
		}
		else if (calcul[b] == 3) {
			buf /= nums[b + 1];
		}

	}
	if (low > buf) {
		low = buf;
	}
	if (high < buf) {
		high = buf;
	}
	return 0;
}



int permu(int k) {
	if (k == M) {

		operation();
		return 0;
	}
	for (int a = k; a < M; a++) {
		buf = calcul[a];
		calcul[a] = calcul[k];
		calcul[k] = buf;
		permu(k + 1);
		buf = calcul[a];
		calcul[a] = calcul[k];
		calcul[k] = buf;
	}
	return 0;
}



int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		low = 999999;
		high = -999999;
		N = 0;
		M = 0;
		buf = 0;
		idx = 0;
		sums = 0;
		for (int i = 0; i < 13; i++) {
			nums[i] = 0;
			calcul[i] = 0;
		}
		scanf("%d", &N);
		for (int i = 0; i < 4; i++) {
			scanf("%d", &opt[i]);
			M += opt[i];
			for (int j = 0; j < opt[i]; j++) {
				if (i == 0) {
					calcul[j + idx] = 0;
				}
				else if (i == 1) {
					calcul[j + idx] = 1;
				}
				else if (i == 2) {
					calcul[j + idx] = 2;
				}
				else if (i == 3) {
					calcul[j + idx] = 3;
				}
			}
			idx += opt[i];

		}
		for (int i = 0; i < M; i++) {
			printf("%d", calcul[i]);
		}
		for (int i = 0; i < N; i++) {
			scanf("%d", &nums[i]);
		}

		permu(0);
		printf("#%d %d\n", M, high-low);
	}



	return 0;
}
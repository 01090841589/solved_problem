#include <stdio.h>

int T, N, M, L;
long long arr[4000002];
long long k, a;
long long c, buf, left, right, sums, b;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf(" %d %d %d", &N, &M, &L);
	k = 1;
	M += L;
	while (true) {
		if (k >= N) {
			break;
		}
		k *= 2;
	}
	for (int i = 0; i < k; i++) {
		arr[i] = 0;
	}

	for (int i = k; i < k+N; i++) {
		scanf(" %lld", &arr[i]);
	}
	for (int i = k + N; i < k * 2; i++) {
		arr[i] = 0;
	}

	for (int i = k * 2 - 1; i > 1; i--) {
		arr[i / 2] += arr[i];
	}
	for (int i = 0; i < M; i++) {
		scanf(" %lld %lld %lld", &a, &b, &c);
		if (a == 1) {
			buf = k + b - 1;
			c = c - arr[buf];
			while (buf > 0) {
				arr[buf] += c;
				buf /= 2;
			}
		}
		else {
			sums = 0;
			left = k+b-1;
			right = k+c-1;
			while (left <= right) {
				if (left % 2 == 1) {
					sums += arr[left];
					left++;
				}
				if (right % 2 == 0) {
					sums += arr[right];
					right--;
				}
				left /= 2;
				right /= 2;
			}
			printf("%lld\n", sums);
		}

	}
	

	return 0;
}
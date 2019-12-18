// 새로운 B index tree 배열을만들어 하나씩카운팅하면서

// 앞에서부터 숫자~N의 총합을 더하기


#include <stdio.h>

int T, N, M;
int arr[400002];
int k, a;
int buf, left, right, sums;
long long res;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf(" %d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf(" %d", &N);
		k = 1;
		res = 0;
		while (true) {
			if (k >= N) {
				break;
			}
			k *= 2;
		}
		for (int i = 0; i < k*2; i++) {
			arr[i] = 0;
		}

		for (int i = 0; i < N; i++) {
			scanf(" %d", &a);
			buf = a + k - 1;
			left = buf + 1;
			right = k * 2 - 1;
			sums = 0;
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
			res += sums;


			while (buf > 0) {
				arr[buf] += 1;
				buf /= 2;
			}
		}
		printf("#%d %lld\n", tc + 1, res);

	}

	return 0;
}
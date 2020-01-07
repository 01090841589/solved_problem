#include <stdio.h>

int T;
long long N, M;
long long judge[10005];
long long left, mid, right, result;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d %d", &N, &M);
		left = 0;
		right = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &judge[i]);
			if (right < judge[i])
				right = judge[i];
		}
		right *= M;
		result = right;
		while (left <= right) {
			mid = (left + right) / 2;
			long long passed = 0;
			for (int i = 0; i < N; i++) {
				passed += mid / judge[i];
			}
			if (M <= passed) {
				right = mid - 1;
				if (result > mid)
					result = mid;
			}
			else {
				left = mid + 1;
			}
		}
		printf("#%d %lld", tc + 1, result);
	}


	return 0;
}
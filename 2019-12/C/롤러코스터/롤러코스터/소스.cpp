#include <stdio.h>

long long rail[200009][2];
int a, b;

void quickSort(int start, int end) {
	int pivot = start, left = start, right = end, tempa, tempb;
	if (start >= end) return;
	while (left <= right) {
		while (rail[pivot][1] * (rail[left][0] - 1) <= rail[left][1] * (rail[pivot][0] - 1)) {
			left++;
			if (left > end) break;

		}
		while (rail[pivot][1] * (rail[right][0] - 1) >= rail[right][1] * (rail[pivot][0] - 1) && right > start) right--;
		if (left > right) {
			tempa = rail[right][0];
			tempb = rail[right][1];
			rail[right][0] = rail[pivot][0];
			rail[right][1] = rail[pivot][1];
			rail[pivot][0] = tempa;
			rail[pivot][1] = tempb;
		}
		else {
			tempa = rail[right][0];
			tempb = rail[right][1];
			rail[right][0] = rail[left][0];
			rail[right][1] = rail[left][1];
			rail[left][0] = tempa;
			rail[left][1] = tempb;
		}
	}
	while (rail[pivot][1] * (rail[left][0] - 1) <= rail[left][1] * (rail[pivot][0] - 1)) left++;
	while (rail[pivot][1] * (rail[right][0] - 1) >= rail[right][1] * (rail[pivot][0] - 1) && rail[start][1] * (rail[right][0] - 1) > rail[right][1] * (rail[start][0] - 1)) right--;
	quickSort(start, right - 1);
	quickSort(right + 1, end);
}


int main() {
	freopen("Text.txt", "r", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++)
	{
		unsigned long long int result = 1;
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%d %d", &rail[i][0], &rail[i][1]);
		}
		quickSort(0, N - 1);
		for (int i = N-1; i >= 0; i--)
			result = ((rail[i][0] * result) % 1000000007 + rail[i][1]) % 1000000007;
		printf("#%d %d\n", tc, result);

	}
	return 0;
}
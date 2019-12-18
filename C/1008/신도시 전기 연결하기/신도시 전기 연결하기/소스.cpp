#include <stdio.h>

#include <stdlib.h>
#include <string.h>

int T, N, K;
int x[100010];
int A[100010];
int B[100010];
int res;
//int Quicksort(int left, int right)
//{
//	int i = left;
//	int j = right;
//	int p = (right - left) / 2 + left;
//	for (int n = left; n <= right; n++)
//	{
//		if (n == p)
//			continue;
//		if (A[n] > A[p])
//		{
//			B[i] = A[n];
//			i++;
//		}
//		if (A[n] <= A[p])
//		{
//			B[j] = A[n];
//			j--;
//		}
//	}
//	B[j] = A[p];
//	p = j;
//	for (int n = left; n <= right; n++)
//		A[n] = B[n];
//	if (left < p - 1)
//		Quicksort(left, p - 1);
//	if (p + 1 < right)
//		Quicksort(p + 1, right);
//	return 0;
//}


int compare(const void * a, const void * b)
{
	return (*(int*)b - *(int*)a);
}


int main() {	
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);

	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		scanf("%d", &K);
		res = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &x[i]);
			if (i > 0) {
				A[i - 1] = x[i] - x[i - 1];
			}
		}
		qsort(A, N-1, sizeof(int), compare);
	/*	Quicksort(0, N-1);*/
		if (N > K) {
			for (int i = (K - 1); i < N; i++) {
				res += A[i];
			}
		}


		for (int i = 0; i < N; i++) {
			A[i] = 0;
		}

		if (N <= K) {
		
			printf("#%d 0\n", tc+1);
		}
		else {
			printf("#%d %d\n", tc+1, res);

		}
	}




	return 0;
}


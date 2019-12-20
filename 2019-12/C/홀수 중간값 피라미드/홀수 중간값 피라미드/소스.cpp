//#include <stdio.h>
//
//int T, N, res;
//int arr[200008];
//int left, right, comp;
//int main() {
//	freopen("Text.txt", "r", stdin);
//	scanf("%d", &T);
//	for (int tc = 0; tc < T; tc++) {
//		scanf("%d", &N);
//		N = N * 2 - 1;
//		for (int i = 0; i < N; i++) {
//			scanf(" %d", &arr[i]);
//		}
//		left = 0;
//		right = N-1;
//		res = (left+right)/2;
//		while (left < right) {
//			comp = 0;
//			for (int i = 0; i < N; i++) {
//				if (arr[i] >= res) {
//					comp++;
//				}
//				else {
//					comp--;
//				}
//			}
//			if (comp >= 1) {
//				left = res+1;
//				res = (left+right)/2;
//			}
//			else {
//				right = res;
//				res = (left + right) / 2;
//			}
//		}
//		printf("#%d %d\n", tc+1, res-1);
//
//
//
//	}
//
//
//	return 0;
//}


#include <stdio.h>
#include <string.h>
#define NM 200015
#define FOR(i,n,m) for (int i=(n);i<=(m);i++)
#define si(n) fscanf(in,"%d",&n)
typedef long long int ll;
using namespace std;

//FILE *in = fopen("input.txt", "r"), *out = fopen("output.txt", "w");
//FILE *in = fopen("input.txt", "r"), *out = stdout;
FILE *in = stdin, *out = stdout;

int n, a[NM], b[NM];
void input() {
	si(n);
	FOR(i, 1, 2 * n - 1) si(a[i]);
}
int check(int X) {
	FOR(i, 1, 2 * n - 1) b[i] = (a[i] >= X) ? 1 : 0;
	for (int p = n - 1, q = n + 1; p >= 1; p--, q++) {
		if (b[p] == b[p + 1]) return b[p];
		if (b[q] == b[q - 1]) return b[q];
	}
	if (n % 2 == 0) return 1 - b[n];
	return b[n];
}

void pro() {
	int l = 1, r = 2 * n - 1, ans = 0, mid;
	while (l <= r) {
		mid = (l + r) / 2;
		if (check(mid)) {
			ans = ans < mid ? mid : ans;
			l = mid + 1;
		}
		else r = mid - 1;
	}
	fprintf(out, "%d\n", ans);
}

int main() {
	freopen("Text.txt", "r", stdin);
	int TT; si(TT);
	FOR(tt, 1, TT) {
		input();

		fprintf(out, "#%d ", tt);
		pro();
	}
	return 0;
}
#include <stdio.h>

int N, M, L;
long long arr[4000020];
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
	for (int i = k; i < k+N; i++) {
		scanf(" %lld", &arr[i]);
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
//
///////////  Indexed Tree /////////
//#include <stdio.h>
//
//int B;
//long long tree[4000020], DEFAULT;
//
//void update_tree(int x, long long cnt, long long f(long long, long long)) {
//	if (x == 0) return;
//
//	tree[x] = f(tree[x], cnt);
//	update_tree(x >> 1, cnt, f);
//}
//long long find_tree(int left, int right, long long f(long long, long long)) {
//	int L = left, R = right;
//	long long res = DEFAULT;
//	while (L <= R) {
//		if (L & 1) res = f(res, tree[L++]);
//		if (!(R & 1)) res = f(res, tree[R--]);
//		L >>= 1, R >>= 1;
//	}
//	return res;
//}
//
//void init(long long size, long long _DEFAULT) {
//	for (B = 1; B < size; B *= 2);
//	B = B - 1;
//	for (int i = 1; i < B * 2 + 1; i++) tree[i] = DEFAULT;
//}
//
//void update(int x, long long cnt, long long f(long long, long long)) {
//	cnt = cnt - tree[x+B];
//	update_tree(x + B, cnt, f); 
//}
//long long find(int left, int right, long long f(long long, long long)) { return find_tree(left + B, right + B, f); }
//long long n, m, l	;
//long long sum(long long x, long long y) { return x + y; }
//
//int main() {
//	//freopen("Text.txt", "r", stdin);
//	scanf(" %lld %lld %lld", &n, &m, &l);
//	m += l;
//	init(n, 0);
//	for (int i = 1; i <= n; i++) {
//		scanf(" %lld", &tree[B + i]);
//	}
//	for (int i = B; i >= 1; i--)
//		tree[i] = sum(tree[i * 2], tree[i * 2 + 1]);
//
//	for (int i = 1; i <= m; i++) {
//		int t, x, y;
//		scanf(" %d %d %d", &t, &x, &y);
//		if (t == 1) {
//
//			update(x, y, sum);
//		}
//		else printf("%lld\n", find(x, y, sum));
//	}
//	printf("\n");
//	return 0;
//}
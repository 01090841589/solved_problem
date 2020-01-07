#include <iostream>
using namespace std;

int main(int argc, char** argv) {
	freopen("Text.txt", "r", stdin);
	int T;
	cin >> T;
	for (int test_case = 1, N, M; test_case <= T; ++test_case) {
		long long m[10001];
		long long max_table = 0;

		cin >> N >> M;
		for (int i = 0; i < N; ++i) {
			cin >> m[i];
			/*max_table = max_table > m[i] ? max_table : m[i];*/
		}

		long long right = 300000000000000000LL;
		long long mid;
		long long left = 0;

		while (left < right) {
			mid = (left + right) / 2;

			long long ans = 0;
			for (int i = 0; i < N; ++i)
				ans += mid / m[i];

			if (ans < M)
				left = mid + 1;
			else {
				right = mid - 1;
			}
		}
		cout << '#' << test_case << ' ' << right << '\n';
	}
	return 0;
}
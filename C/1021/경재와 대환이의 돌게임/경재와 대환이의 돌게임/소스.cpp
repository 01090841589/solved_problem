#include <stdio.h>

int T;
int R, B;
int cnt;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		cnt = 0;
		scanf("%d", &R);
		scanf("%d", &B);
		while (true){
			if (R + B < 2) {
				break;
			}
			if (R > B) {
				R -= 2;
				B += 1;
			}
			else if (R < B) {
				B -= 2;
				R += 1;
			}
			else {
				R -= 2;
				B += 1;
			}
			cnt += 1;
			cnt = cnt%2;
		}
		if (cnt == 0) {
			printf("#%d DH\n", tc + 1);
		}
		else {
			printf("#%d KJ\n", tc + 1);

		}
	}
	return 0;
}
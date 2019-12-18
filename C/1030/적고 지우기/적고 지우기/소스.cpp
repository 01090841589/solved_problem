#include <stdio.h>

int T;
int num[10];
char nums[1002];
int a;
int result;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		result = 0;
		scanf(" %s", &nums);
		a = 0;

		while (true) {
			if (nums[a] == 0) {
				break;
			}
			num[nums[a] - 48] = (num[nums[a] - 48] + 1) % 2;
			a++;
		}
		for (int i = a; i > 0; i--) {
			nums[i] = 0;
		}
		for (int i = 0; i < 10; i++) {
			if (num[i] == 1) {
				result += 1;
			}
			num[i] = 0;
		}

		printf("#%d %d\n", tc + 1, result);
	}
	return 0;
}
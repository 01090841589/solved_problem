#include <stdio.h>

int T;
char start[7];
char arrive[7];
int hour1, minute1, second1;
int hour2, minute2, second2;
int main() {
	freopen("½Ã°£°³³ä.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; ++tc) {
		scanf(" %s", &start);
		scanf(" %s", &arrive);
		hour1 = (start[0] - 48) * 10 + (start[1] - 48);
		minute1 = (start[3] - 48) * 10 + (start[4] - 48);
		second1 = (start[6] - 48) * 10 + (start[7] - 48);
		hour2 = (arrive[0] - 48) * 10 + (arrive[1] - 48);
		minute2 = (arrive[3] - 48) * 10 + (arrive[4] - 48);
		second2 = (arrive[6] - 48) * 10 + (arrive[7] - 48);

		if (second2 - second1 < 0) {
			second2 += 60;
			minute2 -= 1;
		}
		if (minute2 - minute1 < 0) {
			minute2 += 60;
			hour2 -= 1;
		}
		if (hour2 - hour1 < 0) {
			hour2 += 24;
		}
		
		second2 -= second1;
		minute2 -= minute1;
		hour2 -= hour1;
		arrive[0] = (hour2 / 10) + 48;
		arrive[1] = (hour2 % 10) + 48;
		arrive[3] = (minute2 / 10) + 48;
		arrive[4] = (minute2 % 10) + 48;
		arrive[6] = (second2 / 10) + 48;
		arrive[7] = (second2 % 10) + 48;
		printf("#%d %s\n", tc+1, arrive);
	}
}
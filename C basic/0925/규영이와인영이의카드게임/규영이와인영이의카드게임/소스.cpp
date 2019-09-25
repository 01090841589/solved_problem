#include <stdio.h>
int card[10];
int op_card[10];
int all_card[18];
int visited[10];
int tmp;
int me_win;
int you_win;
int verse() {
	int me = 0;
	int you = 0;

	for (int i = 0; i < 9; i++) {
		if (card[i] > op_card[i]) {
			me += (card[i] + op_card[i]);
		}
		else if (card[i] < op_card[i]) {
			you += (op_card[i] + card[i]);
		}
	}
	if (me > you) {
		me_win += 1;
	}
	else if (you > me) {
		you_win += 1;
	}
	return 0;
}


int permu(int k, int N) {
	if (k == N) {
		verse();
		return 0;
	}
	for (int x = k; x < N; x++) {
		tmp = op_card[x];
		op_card[x] = op_card[k];
		op_card[k] = tmp;
		permu(k + 1, N); 
		tmp = op_card[x];
		op_card[x] = op_card[k];
		op_card[k] = tmp;

	}
}


int main() {
	int T;
	freopen("카드게임.txt", "r", stdin);
	scanf("%d", &T);
	for (int i = 0; i < 18; i++) {
		all_card[i] = i + 1;
	}


	for (int tc = 0; tc < T; tc++) {
		for (int i = 0; i < 9; i++) {
			scanf("%d", &card[i]);
		}
		int flag;
		int a = 0;
		for (int i = 0; i < 18; i++) {
			flag = 1;
			for (int j = 0; j < 9; j++) {
				if (all_card[i] == card[j]) {
					flag = 0;
					break;
				}
			}
			if (flag) {
				op_card[a] = i + 1;
				a += 1;
			}
		}
		me_win = 0;
		you_win = 0;
		permu(0, 9);




		printf("#%d %d %d\n", tc + 1, me_win, you_win);
	}

	return 0;
}
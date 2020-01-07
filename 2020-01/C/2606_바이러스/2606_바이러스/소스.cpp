#include <stdio.h>

int N, M;
int com1, com2;
int MAP[101][101];
int queue[10000];
int visited[100];
int rear, res, now;
int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &N);
	scanf("%d", &M);
	res = 0;
	for (int i = 0; i < M; i++) {
		scanf("%d %d", &com1, &com2);
		MAP[com1][com2] = 1;
		MAP[com2][com1] = 1;
	}
	queue[0] = 1;
	rear = 1;
	visited[1] = 1;
	while (rear) {
		rear--;
		now = queue[rear];
		for (int i = 1; i < N+1; i++) {
			if (MAP[now][i] && visited[i] == 0) {
				queue[rear] = i;
				rear++;
				res++;
				visited[i] = 1;
			}
		}
	}
	printf("%d", res);
	return 0;
}
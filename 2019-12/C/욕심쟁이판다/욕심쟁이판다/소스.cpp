#include <stdio.h>
#include <algorithm>
using namespace std;

int bamboo[500][500];
int Dp[500][500];
int dx[4] = { 0,0,-1,1 };
int dy[4] = { -1,1,0,0 };
int n, day = 1;

int dfs(int y, int x)
{
	if (Dp[y][x] != -1) return Dp[y][x];
	Dp[y][x] = 1;
	for (int i = 0; i < 4; i++)
	{
		int next_x = x + dx[i];
		int next_y = y + dy[i];
		if (next_x >= 0 && next_x < n && next_y >= 0 && next_y < n && (bamboo[y][x] < bamboo[next_y][next_x]))
		{
			int temp = 1;
			temp += dfs(next_y, next_x);
			Dp[y][x] = max(Dp[y][x], temp);
			if (Dp[y][x] > day) day = Dp[y][x];

		}
	}
	return Dp[y][x];
}

int main(void)
{
	freopen("Text.txt", "r", stdin);
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &bamboo[i][j]);
			Dp[i][j] = -1;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (Dp[i][j] == -1)
				dfs(i, j);
		}
	}
	printf("%d", day);
	return 0;
}
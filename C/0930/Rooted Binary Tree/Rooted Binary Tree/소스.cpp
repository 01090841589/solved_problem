#include <stdio.h>



int T, K;
int A;
int node[1024];
int tree[1024];
int visited[1024];
int stack[1024];
int Q, idx;
int level;
int search_tree(int depth, int leng) {
	leng = leng / 2;
	if (leng == 0) {
		return 0;
	}
	Q = -1;
	for (int i = 0; i < A; i++) {
		Q += leng;
		if (Q >= A) {
			break;
		}
		if (visited[Q] == 0) {
			visited[Q] = 1;
			tree[idx] = node[Q];
			idx++;
		}

	}
	search_tree(depth, leng);




	return 0;
}



int main() {
	freopen("RTB.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &K);
		
		A = 1;
		for (int i = 0; i < K; i++) {
			A = A*2;
		}
		A -= 1;

		for (int i = 0; i < A; i++) {
			scanf("%d", &node[i]);

			visited[i] = 0;
		}
		idx = 0;
		search_tree(A, A+1);

		printf("#%d ", tc+1);

		level = 1;
		idx = 0;
		for (int i = 0; i < K; i++) {
			for (int j = 0; j < level; j++) {
				printf("%d ", tree[idx]);
				idx++;
			}
			printf("\n");
			level *= 2;

		}	
	}


	return 0;
}
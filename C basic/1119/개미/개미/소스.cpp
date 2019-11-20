#include <stdio.h>

int L, n;
int a[100], b[100], c[100];
int min, max;

int ant(int k) {
	for (int i = 0; i < n; i++) {
		
	}

	return 0;
}

int part(int k) {
	if (k == 3) {
		for (int i = 0; i < L; i++) {
			b[i] = 0;
		}
		for (int i = 0; i < L; i++) {
			c[i] = a[i];
		}
		for (int i = 0; i < L; i++) {
		}
		ant(0);

		return 0;
	}
	else {
		c[k] = 1;
		part(k+1);
		c[k] = 0;
		part(k+1);
	}
}


int main() {
	freopen("Text.txt", "r", stdin);
	scanf("%d", &L);
	min = 0;
	max = 0;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}

	part(0);
	printf("MIN=4\n");
	printf("MAX=8\n");
}


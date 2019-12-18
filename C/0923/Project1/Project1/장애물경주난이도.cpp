/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// scanf("%d&", &a);                      // int 변수 1개 입력받는 예제
// scanf("%f %f", &b, &c);               // float 변수 2개 입력받는 예제 
// scanf("%lf %lf %lf;", &d, &e, &f);     // double 변수 3개 입력받는 예제
// scanf("%c", &g);                      // char 변수 1개 입력받는 예제
// scanf("%s", &var);                    // 문자열 1개 입력받는 예제
// scanf("%lld", &AB);                   // long long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// float b = 1.0, c = 2.0;               
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = 'ABCDEFG';
// long long AB = 12345678901234567L;
// printf("%d", a);                      // int 변수 1개 출력하는 예제
// printf("%f %f", b, c);                // float 변수 2개 출력하는 예제
// printf("%lf %lf %lf", d, e, f);       // double 변수 3개 출력하는 예제
// printf("%c", g);                      // char 변수 1개 출력하는 예제
// printf("%s", var);                    // 문자열 1개 출력하는 예제
// printf("%lld", AB);                   // long long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////




#include <stdio.h>
int a[100];
int main(void)
{
	int T;
	int i = 0;
	setbuf(stdout, NULL);
	freopen("장애물.txt", "r", stdin);
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		int N = 0;
		scanf("%d", &N);
		for (i = 0; i < N; i++) {
			scanf("%d", &a[i]);
		}
		int high = 0;
		int low = 0;
		int buf = 0;
		for (i = 0; i < N-1; i++) {
			if (a[i] - a[i + 1] > 0) {
				if (high < a[i] - a[i + 1]) {
					high = a[i] - a[i + 1];
				}
			else {
				if (low < a[i+1] - a[i]) {
					low = a[i + 1] - a[i];
			}
			}
		}

	}
	printf("#%d %d\n", j + 1, a[j]);
	}
	return 0;
}
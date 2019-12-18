
#include <stdio.h>
#define max 1000000 //최대 입력 개수



int Quicksort(int left, int right);
int T;
int A[max];
int B[max];
int result;


int main()
{
	freopen("Text.txt", "r", stdin);
	scanf_s("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		result = 0;
		int n; //입력할 숫자 개수
		scanf_s("%d", &n);
		for (int i = 0; i < n; i++) //숫자를 입력받아 배열 A에 저장
			scanf_s("%d", &A[i]);
		Quicksort(0, n - 1); //정렬 시작
		for (int i = 0; i < n; i++) //결과 출력
			result += A[i];
		result += n;
		result += A[n - 1];
		printf("#%d %d\n", tc+1, result);
	}

	return 0;

}


int Quicksort(int left, int right)
{
	int i = left; //작은 숫자부터 1씩 증가하기 위한 변수
	int j = right; //큰 숫자부터 1씩 감소하기 위한 변수
	int p = (right - left) / 2 + left; //피봇(입력받은 배열의 가운데를 기준)
	for (int n = left; n <= right; n++) //A배열의 숫자를 피봇과 비교
	{
		if (n == p) //피봇을 만나면 보류하고 넘어감
			continue;
		if (A[n] <= A[p]) //피봇보다 작거나 같은 수는 배열 B의 앞쪽부터 저장
		{
			B[i] = A[n];
			i++;
		}
		if (A[n] > A[p]) //피봇보다 큰 수는 배열 B의 뒤쪽부터 저장
		{
			B[j] = A[n];
			j--;
		}
	}
	B[j] = A[p]; //배열 B의 마지막 남은 곳에 피봇 저장
	p = j; //피봇의 위치 수정
	for (int n = left; n <= right; n++) //정렬된 배열 B를 배열 A에 복사
		A[n] = B[n];
	if (left < p - 1) //피봇보다 작은 숫자를 다시 정렬
		Quicksort(left, p - 1);
	if (p + 1 < right) //피봇보다 큰 숫자를 다시 정렬
		Quicksort(p + 1, right);
	return 0;
}
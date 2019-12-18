#include <stdio.h> 
#define parent(x) (x-1)/2 
void heap(int *data, int num){ 
	for(int i=1; i<num; i++){ 
		int child = i; 
		while(child > 0){ 
			int root = parent(child); 
			if(data[root] < data[child]){ 
				int temp = data[root]; 
				data[root] = data[child]; 
				data[child] = temp; 
			} 
			child = root; 
		} 
	} 
} 
int main(void){ 
	int num = 9; 
	int data[] = {15, 4, 8, 11, 6, 3, 1, 6, 5}; 
	heap(data, num); // 힙을 만든다. 
	for(int i=num-1; i>=0; i--){ 
		// 가장큰 숫자(root)를 맨 마지막 원소와 스왑 
		int temp = data[i]; 
		data[i] = data[0]; 
		data[0] = temp; 
		
		// 맨마지막원소(가장큰원소)를 제외하고 다시 힙을 만든다. 
		heap(data, i); 
	} 
	
	// 결과 출력 
	for(int i=0; i<num; i++){ 
		printf("%d ", data[i]); 
	} 
	return 0; 
}

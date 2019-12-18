#include <stdio.h>

struct NODE {
	int next[26];
	int cnt;
	void init() {
		for (int i = 0; i < 26; i++) {
			next[i] = -1;
		}
		cnt = 0;
	}
}trie[NM];
int root = 0, trieN;
//트라이는 캐시메모리 cache friendly(메모리가 건너뛰어짐, 캐시충돌로 느려짐) 포인터로 만들면 안된다, memory locality

void init(void) {
	root = 0;
	trieN = 0;
	trie[0].init();
}

void myInsert(int trieIdx, int bufIdx, int buffer_size, char *buf) {
	trie[trieIdx].cnt++;
	if (bufIdx == buffer_size) return; // 단어가 끝난위치. 필요하다면 색칠하는 코드 필요
	int ch = buf[bufIdx] - 'a';

	if (trie[trieIdx].next[ch] == -1) { //자식이 없으면 생성, 정적으로 생성. new로 만들수도 있지만 매우 느리다.
		trie[trieIdx].next[ch] = ++trieN;
		trie[trieN].init();
	}

	myInsert(trie[trieIdx].next[ch], bufIdx + 1, buffer_size, buf); // 자식이있으면 가서 탐색
}
void insert(int buffer_size, char *buf) {
	myInsert(root, 0, buffer_size, buf);
}

int query(int buffer_size, char *buf) {
	int trieIdx = root;
	for (int i = 0; i < buffer_size; i++) {
		int ch = buf[i] - 'a';
		trieIdx = trie[trieIdx].next[ch];
		if (trieIdx == -1) return 0;
	}
	return trie[trieIdx].cnt;
}
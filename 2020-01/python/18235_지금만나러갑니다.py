import sys
sys.stdin = open("지금만나러갑니다.txt")

from collections import deque


N, A, B = map(int,input().split())
duck1 = [0]*N
duck2 = [0]*N
duck1[A-1] = 1
duck2[B-1] = 1

que = deque()
que.append([A-1, 1])
while que:
    site, turn = que.popleft()
    if 0 <= site-turn:
        duck1[site-turn] += turn*2
        que.append([site-turn, turn*2])
    if site+turn < N:
        duck1[site+turn] += turn*2
        que.append([site+turn, turn*2])
que.append([B-1, 1])
while que:
    site, turn = que.popleft()
    if 0 <= site-turn:
        duck2[site-turn] += turn*2
        que.append([site-turn, turn*2])
    if site+turn < N:
        duck2[site+turn] += turn*2
        que.append([site+turn, turn*2])
res = 1000000
for i in range(N):
    if (duck1[i] & duck2[i]) > 0:
        result = 0
        days = duck1[i] & duck2[i]
        while True:
            if days % 2 == 1:
                break
            else:
                days = days >> 1
                result += 1
        if result != 0 and res > result:
            res = result
if res == 1000000:
    print(-1)
else:
    print(res)

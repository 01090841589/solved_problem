import sys
sys.stdin = open("계단오르기.txt")


from collections import deque

N = int(input())
stair = []
for i in range(N):
    stair.append(int(input()))
stair.insert(0, 0)
stair.append(0)
stair.append(0)
stair.append(0)
stair_scr = [0] * (N+4)
queue = deque()
queue.append([0, 0, 0])
while queue:
    n, scr, k = queue.popleft()
    if n == 1:
        k = 0
    if n == N:
        if stair_scr[n] < scr:
            stair_scr[n] = scr
    if k == 0 and n > 0:
        if stair_scr[n] < scr:
            stair_scr[n] = scr
        else:
            continue
    if n > N:
        continue
    if k < 1:
        queue.append([n+1, scr+stair[n+1], k+1])
    queue.append([n+2, scr+stair[n+2], 0])
print(stair_scr[N])
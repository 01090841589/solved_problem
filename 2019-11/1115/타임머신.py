import sys
sys.stdin = open("타임머신.txt")

from collections import deque
def bellman():
    global turn
    flag = 0
    for i in node:
        if i[0] == 1:
            flag = 1
    if flag:
        for c in node:
            if dist[c[0]]+c[2] < dist[c[1]]:
                dist[c[1]] = dist[c[0]]+c[2]
    else:
        turn = -1

N, M = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(M)]
dist = [999999] * (N+1)
dist[1] = 0
turn = 0
while True:
    turn += 1
    past = dist[:]
    bellman()
    if turn == -1:
        break
    if past == dist:
        break
    if turn > M+1:
        turn = -1
        break

if turn != -1:
    for i in range(2, N+1):
        if dist[i] > 100000:
            print(-1)
        else:
            print(dist[i])
else:
    comp = [i for i in range(2, N+1)]
    que = deque([1])
    while que:
        n = que.popleft()
        for c in node:
            if c[0] == n and c[1] in comp:
                comp.remove(c[1])
                que.append(c[1])

    if comp and dist[1] == 0:
        for i in range(2, N+1):
            if dist[i] > 100000:
                print(-1)
            else:
                print(dist[i])

    else:
        print(-1)
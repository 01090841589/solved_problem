import sys
sys.stdin = open("민준이와마산그리고건우.txt")


from collections import deque

V, E, P = map(int, input().split())
MAP = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    MAP[a].append([b, c])
    MAP[b].append([a, c])
que = deque()
que.append([1, 0, 0])
visited = [10000*V] * (V+1)
visited[1] = 0
flag = 0
res = 10000*V
while que:
    nod, scr, konu = que.popleft()
    for arr in MAP[nod]:
        if arr[0] == V:
            if res > scr+arr[1]:
                res = scr+arr[1]
                flag = konu
            elif res == scr+arr[1] and konu == 1:
                flag = konu
            continue
        if visited[arr[0]] > scr + arr[1]:
            visited[arr[0]] = scr + arr[1]
            if arr[0] == P:
                que.append([arr[0], scr + arr[1], 1])
            else:
                que.append([arr[0], scr + arr[1], konu])
        elif visited[arr[0]] == scr + arr[1] and konu == 1:
            que.append([arr[0], scr + arr[1], konu])
if P == 1 or P == V:
    flag = 1
if flag:
    print("SAVE HIM")
else:
    print("GOOD BYE")
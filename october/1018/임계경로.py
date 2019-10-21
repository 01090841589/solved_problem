import sys
sys.stdin = open("임계경로.txt")

def road(S):
    global buf, result
    stack = [[S, 0, []]]
    while stack:
        [S, scr, gone] = stack.pop()
        for i in range(1, N+1):
            if MAP[S][i] > 0:
                if i == G:
                    if buf < scr+MAP[S][i]:
                        buf = scr+MAP[S][i]
                        result = set(gone+[str(S)+str(i)])
                    elif buf == scr+MAP[S][i]:
                        result.update(gone+[str(S)+str(i)])

                else:
                    stack.append([i, scr+MAP[S][i], gone+[str(S)+str(i)]])



N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(M)]
S, G = map(int, input().split())
buf = 0
MAP = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    MAP[arr[i][0]][arr[i][1]] = arr[i][2]
result = set()
road(S)
print(buf)
print(len(result))

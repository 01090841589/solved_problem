import sys
sys.stdin = open('카운슬러.txt')

def meet(k, scr):
    if k == N:
        if result < scr:
            result = scr
        return
    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        meet()


T = int(input())
for tc in range(1, 2):
    N = int(input())
    worm = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [0] * N
    meet(0, 0)
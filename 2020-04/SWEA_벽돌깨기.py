import sys
sys.stdin = open("벽돌꺠기.txt")

def mapReset():
    for h in range(H):
        for w in range(W):
            MAP_NOW[h][w] = MAP[h][w]

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    MAP = [[0] for _ in range(H)]
    MAP_NOW = [[0]*W for _ in range(H)]
    for i in range(H):
        MAP[i] = list(map(int, input().split()))


    for i in range(N):
        mapReset()

    [print(MAP_NOW[i]) for i in range(H)]

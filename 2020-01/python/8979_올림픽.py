import sys
sys.stdin = open("올림픽.txt")


N, M = map(int,input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
rank = 0
score = [[0, 0] for _ in range(N)]

for i in range(N):
    score[i][0] = MAP[i][0]
    score[i][1] = MAP[i][1]*100000000000000+MAP[i][2]*10000000+MAP[i][3]
score.sort(key=lambda k:k[1], reverse=True)
for i in range(N):
    if i > 0:
        if score[i][1] < score[i-1][1]:
            rank = i
    if score[i][0] == M:
        print(rank+1)
        break
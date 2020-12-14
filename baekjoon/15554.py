import sys
sys.stdin = open("15554.txt")


N = int(input())
pic = []
for i in range(N):
    pic.append(list(map(int, input().split())))
val = [0]*(N)
pic.sort()
val[0] = pic[0][1]
for i in range(1, N):
    val[i] = val[i-1]+pic[i][1]
res = 0
minv, maxv = pic[0][0], pic[0][0]
for i in range(N):
    maxv = pic[i][0]

    S = val[i] - maxv + minv
    res = max(res, S)
    if i == N-1: break
    minv = max(minv, pic[i+1][0]-val[i])

print(res)
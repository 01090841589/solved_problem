import sys
sys.stdin = open("2096.txt")


N = int(input())


bufmax, bufmin = [0] * 3, [0]*3
minx, maxx = 999999, 0
visitedmax, visitedmin = [], []
for y in range(N):
    inp = list(map(int, input().split()))
    if y == 0:
        visitedmax = inp[:]
        visitedmin = inp[:]
        continue
    bufmax[0] = inp[0] + max(visitedmax[0], visitedmax[1])
    bufmax[1] = inp[1] + max(visitedmax[0], visitedmax[1], visitedmax[2])
    bufmax[2] = inp[2] + max(visitedmax[2], visitedmax[1])
    bufmin[0] = inp[0] + min(visitedmin[0], visitedmin[1])
    bufmin[1] = inp[1] + min(visitedmin[0], visitedmin[1], visitedmin[2])
    bufmin[2] = inp[2] + min(visitedmin[2], visitedmin[1])
    visitedmax = bufmax[:]
    visitedmin = bufmin[:]

maxx = max(visitedmax)
minx = min(visitedmin)



print(maxx, minx)





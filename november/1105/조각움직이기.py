import sys
sys.stdin = open("조각움직이기")


from itertools import permutations
MAP = [list(input()) for _ in range(5)]
DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def calcul():
    global result
    arrive = []
    for y in range(5):
        for x in range(5):
            if visited[y][x] == 1:
                arrive.append([y, x])
    for a in permutations(range(5), 5):
        scr = 0
        for i in range(5):
            scr += abs(arrive[i][0]-dots[a[i]][0]) + abs(arrive[i][1]-dots[a[i]][1])
        if result > scr:
            result = scr



def fives(y, x, k):
    global cnt
    if k == 0:
        calcul()
        cnt += 1
        return
    for c in DIR:
        Y = y+c[0]
        X = x+c[1]
        if 0 <= Y < 5 and 0 <= X < 5 and visited[Y][X] == 0:
            visited[Y][X] = 1
            fives(Y, X, k-1)
            visited[Y][X] = 0



dots = []
for y in range(5):
    for x in range(5):
        if MAP[y][x] == '*':
            dots.append([y, x])
result = 5*5*5
lent = [0, 0, 1, 2, 4, 6]
if len(dots) < 5:
    for y in range(5):
        for x in range(5):
            scr = 0
            for c in dots:
                scr += (abs(y-c[0])+abs(x-c[1]))
            if result > scr:
                result = scr
    print(result-lent[len(dots)])
else:
    cnt = 0
    visited = [[0]*5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            visited[y][x] = 1
            fives(y, x, 4)
            visited[y][x] = 0
    print(result)
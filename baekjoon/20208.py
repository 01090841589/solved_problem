import sys
sys.stdin = open("20208.txt")


def get_milk(y, x, life, key, scr):
    global res
    if abs(home[0]-y)+abs(home[1]-x) <= life:
        if res < scr:
            res = scr
    for i in range(milks):
        if (key >> i) & 1:
            if life >= (abs(y-milk[i][0])+abs(x-milk[i][1])):
                if i == 7:
                    pass
                get_milk(milk[i][0], milk[i][1], life - (abs(y-milk[i][0])+abs(x-milk[i][1]))+H, key - (1 << i), scr+1)
N, M, H = map(int, input().split())
res = 0
MAP = [list(map(int, input().split())) for _ in range(N)]
milk = []
home = []
for y in range(N):
    for x in range(N):
        if MAP[y][x] == 2:
            milk.append([y, x])
        elif MAP[y][x]:
            home = [y, x]
key = 0
milks = len(milk)
for i in range(milks):
    key += (1<<i)
get_milk(home[0], home[1], M, key, 0)
print(res)
import sys
sys.stdin = open("게리멘더링.txt")


def calcul(y, x, led, red):
    global result
    reg1, reg2, reg3, reg4, reg5 = 0, 0, 0, 0, 0
    lreg, rreg = 0, 0
    for dy in range(N):
        for dx in range(N):
            if dy < y:
                if dx <= led:
                    reg1 += MAP[y][x]
                else:
                    reg2 += MAP[y][x]
            elif dy > y+led+red:
                if dx < led:
                    reg3 += MAP[y][x]
                else:
                    reg4 += MAP[y][x]
            else:
                lreg = dx, rreg = dx
                if dx < lreg:
                    reg1 += MAP[y][x]
                elif lreg <= dx <= rreg:
                    reg5 += MAP[y][x]
                elif dx > rreg:
                    reg2 += MAP[y][x]
    print(reg1, reg2, reg3, reg4, reg5)

def gerry(y, x, led, red):
    if led + red > N:
        return
    if x-led >= 0 and y+red < N and x-led+red+1 < N:
        calcul(y, x, led, red)
        gerry(y, x, led+1, red)
        gerry(y, x, led, red+1)



N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]

[print(MAP[i]) for i in range(N)]

result = 100*N*N

for y in range(N):
    for x in range(N):
        gerry(y, x, 1, 1)

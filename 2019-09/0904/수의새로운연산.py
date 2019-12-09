import sys
sys.stdin = open('수.txt')
MAP = [[0]*300 for _ in range(300)]
y, x = 1, 1
MAP[y][x] = 1
for i in range(2, 44444):
    if y == 1:
        y += x
        x = 1
        MAP[y][x] = i
    else:
        y -= 1
        x += 1
        MAP[y][x] = i

[print(MAP[i]) for i in range(300)]

T = int(input())
for tc in range(1, 2):
    p, q = map(int, input().split())
    dots = []
    MAP.index(p)
    for y in range(300):
        for x in range(300):
            if MAP[y][x] == p:
                dots.append([y, x])
            if MAP[y][x] == q:
                dots.append([y, x])
            if len(dots) == 2:
                break
        if len(dots) == 2:
            break
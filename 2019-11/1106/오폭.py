import sys
sys.stdin = open("오목.txt")

DIR = [[0, 1], [1, 1], [1, 0], [-1, 1]]
DIRn = [[0, -1], [-1, -1], [-1, 0], [1, -1]]
def five_stone(y, x, k):
    n = 1
    for c in DIR:
        if n == 5:
            break
        n = 1
        while True:
            Y = y+c[0]*n
            X = x+c[1]*n
            if 0 <= Y < 19 and 0 <= X < 19 and MAP[Y][X] == k:
                if n == 1:
                    revY = y-c[0]
                    revX = x-c[1]
                    if 0 <= revY < 19 and 0 <= revX < 19 and MAP[revY][revX] == k:
                        break
                n += 1
            else:
                break
    if n == 5:
        return True
    else:
        return False




MAP = [list(map(int, input().split())) for _ in range(19)]

result = 1
for x in range(19):
    for y in range(19):
        if MAP[y][x] != 0:
            if five_stone(y, x, MAP[y][x]):
                result = 0
                print(MAP[y][x])
                print(y+1, x+1)
if result:
    print(0)
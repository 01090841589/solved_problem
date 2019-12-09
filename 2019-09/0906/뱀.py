import sys
sys.stdin = open('뱀.txt')

DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]



N = int(input())
a = int(input())
apple = [list(map(int, input().split())) for _ in range(a)]
s = int(input())
snake = [list(map(str, input().split())) for _ in range(s)]
snake.append([-1])

MAP = [[0]*N for _ in range(N)]
for i in apple:
    MAP[i[0]-1][i[1]-1] = 9
MAP[0][0] = 1
stack = [[0, 0, 0, 0]]
long = [[0, 0]]
while True:
    [y, x, t, c] = stack.pop(0)
    t += 1
    y += DIR[c][0]
    x += DIR[c][1]
    if t == int(snake[0][0]):
        if snake[0][1] == 'L':
            c = (c + 3) % 4
        else:
            c = (c + 1) % 4
        snake.pop(0)
    if 0 <= y < N and 0 <= x < N and MAP[y][x] != 1:
        if MAP[y][x] == 9:
            MAP[y][x] = 1
            long.append([y, x])
        else:
            Y, X = long.pop(0)
            MAP[Y][X] = 0
            MAP[y][x] = 1
            long.append([y, x])
        stack.append([y, x, t, c])
    else:
        break
print(t)
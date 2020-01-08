import sys
sys.stdin = open("당구공을넣자.txt")

N, M, x, y, dx, dy = map(int, input().split())
crash = 0
y = M - y
DIR = [-dy, dx]
step = 0
while True:
    if step > (N+M)*5:
        crash = -1
        break
    step += 1
    y += DIR[0]
    while y < 0 or y > M:
        if y < 0:
            crash += 1
            DIR[0] *= -1
            y *= -1
        elif y > M:
            crash += 1
            DIR[0] *= -1
            y -= (y - M)*2
    x += DIR[1]
    while x < 0 or x > N:
        if x < 0:
            crash += 1
            DIR[1] *= -1
            x *= -1
        elif x > N:
            crash += 1
            DIR[1] *= -1
            x -= (x - N)*2
    if [y, x] in [[0, 0], [0, N], [M, 0], [M, N]]:
        crash += 1
        break
print(crash)

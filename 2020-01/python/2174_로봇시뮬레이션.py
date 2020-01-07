import sys
sys.stdin = open("로봇시뮬레이션.txt")

arr = ["E", "S", "W", "N"]
DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

A, B = map(int, input().split())
MAP = [[0 for __ in range(A)] for _ in range(B)]
N, M = map(int, input().split())
robots = [[0, 0, 0] for _ in range(N)]
for i in range(N):
    x, y, arrs = map(str, input().split())
    x = int(x)-1
    y = B-int(y)
    arrs = arr.index(arrs)
    MAP[y][x] = i+1
    robots[i] = [y, x, arrs]
flag = 0
for i in range(M):
    if flag:
        break
    rob, comm, repeat = map(str, input().split())
    rob = int(rob)
    repeat = int(repeat)
    y, x, arrs = robots[rob-1]
    if comm == "F":
        MAP[y][x] = 0
        for i in range(repeat):
            y += DIR[arrs][0]
            x += DIR[arrs][1]
            if 0 <= y < B and 0 <= x < A:
                if MAP[y][x] != 0:
                    print("Robot {} crashes into robot {}".format(rob, MAP[y][x]))
                    flag = 1
                    break
            else:
                print("Robot {} crashes into the wall".format(rob))
                flag = 1
                break
        if 0 <= y < B and 0 <= x < A:
            MAP[y][x] = rob
            robots[rob-1] = [y, x, arrs]

    elif comm == "L":
        robots[rob - 1][2] = (robots[rob-1][2] - repeat) % 4
    elif comm == "R":
        robots[rob-1][2] = (robots[rob-1][2] + repeat) % 4

if flag == 0:
    print("OK")
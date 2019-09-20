import sys
sys.stdin = open("최종평가.txt")

T = int(input())
for tc in range(1, 2):
    R, N, K = map(int, input().split())
    MAP = [[0] * R for _ in range(R)]
    robot = [list(map(int, input().split())) for _ in range(N)]
    for rob in robot:
        MAP[rob[0]-1][rob[1]-1] = 1
    [print(MAP[i]) for i in range(R)]

    for a in robot:
        print(a)
        for i in range(R):
            print(0, i, abs(a[0]-1-0), abs(a[1]-1-i))
        for i in range(1, R):
            print(i, R-1, abs(a[0]-1-i), abs(a[1]-1-(R-1)))
        for i in range(R-2, -1, -1):
            print(R-1, i, abs(a[0]-1-(R-1)), abs(a[1]-1-i))
        for i in range(R-2, -1, -1):
            print(i, 0, abs(a[0]-1-i), abs(a[1]-1-0))
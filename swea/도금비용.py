import sys
sys.stdin = open('도금비용.txt')

price = [int((i ** 2) / 2 + (2 * i) / 3 + 1) for i in range(100)]
price.insert(0, 0)


def gold():


T = int(input())
for tc in range(1, 4):
    N = int(input())
    MAP = [[0]*(N) for _ in range(N)]
    M = int(input())
    punk = list(map(int, input().split()))
    for i in range(M):
        MAP[punk[i*2]-1][punk[i*2+1]-1] = 1
    print()
    [print(MAP[i]) for i in range(N)]

    result = price[N]
    for a in range(N-1, 0, -1):
        for y in range(N-a+1):
            for x in range(N-a+1):
                print(y, x, end = '   ')
        print()

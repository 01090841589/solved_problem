# import sys
# sys.stdin = open('foreign.txt')


# N,M = map(int,input().split())
# floor = [list(map(int,input().split())) for _ in range(N)]
# S = int(input())
# coordinates = [list(map(int, input().split()))for _ in range(S)]
#
# for i in range(S):
#     sums = 0
#     for y in range(coordinates[i][0]-1, coordinates[i][2]):
#         for x in range(coordinates[i][1]-1, coordinates[i][3]):
#             sums += floor[y][x]
#     print(sums)

floor = [input()for _ in range(10)]
cnt = 0
res = 0

for y in range(10):
    for x in range(10):
        if floor[y][x] == 'O':
            cnt = 0

            for yy in range(yy,10):
                for xx in range(xx,10):
                    if floor[y][xx] == 'O':
                        cnt += 1
                    if cnt == 4:
                        break

            for yy in range(yy,10):
                for xx in range(xx,10):
                    if floor[yy][x] == 'O':
                        cnt += 1
                    if cnt == 4:
                        break

            for a in range(10):
                if floor[y+a][x+a] == 'O':



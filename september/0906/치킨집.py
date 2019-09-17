import sys
sys.stdin = open('치킨집.txt')

import itertools

N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
result = 99999999999
for y in range(N):
    for x in range(N):
        if MAP[y][x] == 1:
            home.append([y, x])
        elif MAP[y][x] == 2:
            chicken.append([y, x])
for p in itertools.combinations(range(len(chicken)), K):
    dis_sum = 0
    for person in home:
        cho_dis = 9999999
        for chi in p:
            dis = abs(person[0]-chicken[chi][0])+abs(person[1]-chicken[chi][1])
            if cho_dis > dis:
                cho_dis = dis
        dis_sum += cho_dis
    if result > dis_sum:
        result = dis_sum
print(result)
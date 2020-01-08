import sys
sys.stdin = open("단어암기.txt")

import sys
N, M = map(int, sys.stdin.readline().split())
dic = []
MAP = [[0]*28 for _ in range(N)]
for i in range(N):
    dic.append(input())
    for j in range(len(dic[i])):
        MAP[i][0] = len(dic[i])
        MAP[i][1] = len(dic[i])
        MAP[i][ord(dic[i][j])-95] = 1

for i in range(M):
    comm, spell = map(str, sys.stdin.readline().split())
    if comm == '1':
        ind = ord(spell)-95
        res = 0
        for j in range(N):
            if MAP[j][ind] == 1:
                MAP[j][ind] = -1
                MAP[j][1] -= 1
            if MAP[j][0] == MAP[j][1]:
                res += 1
        print(res)
    else:
        ind = ord(spell)-95
        res = 0
        for j in range(N):
            if MAP[j][ind] == -1:
                MAP[j][ind] = 1
                MAP[j][1] += 1
            if MAP[j][0] == MAP[j][1]:
                res += 1
        print(res)
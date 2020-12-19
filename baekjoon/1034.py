import sys
sys.stdin = open("1034.txt")

from collections import defaultdict

lamp_state = dict()

N, M = map(int, input().split())

MAP = [input() for _ in range(N)]
K = int(input())
for i in range(N):
    if lamp_state.get(int("0b"+MAP[i], 2)):
        lamp_state[int("0b" + MAP[i], 2)][0] += 1
    else:
        lamp_state[int("0b"+MAP[i], 2)] = [1, MAP[i].count("0")]

res = 0
for key, val in lamp_state.items():
    if K >= val[1] and K % 2 == val[1] % 2:
        if res < val[0]:
            res = val[0]
print(res)
import sys
sys.stdin = open("근손실.TXT")

from itertools import permutations


def eat(lis):
    now = 0
    for i in lis:
        if now+i-K < 0:
            return False
        now += i - K
    return True


N, K = map(int, input().split())
cals = list(map(int, input().split()))
res = 0
for cal in permutations(cals, N):
    if eat(cal):
        res += 1
print(res)
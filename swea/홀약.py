import sys
sys.stdin = open("홀약.txt")


def odd(x):
    odds = [i if i % 2 else 0 for i in range(1, x + 1)]
    oddsum = [0 for i in range(x)]

    for i in range(len(odds)):
        if odds[i] == 0:
            oddsum[i] += oddsum[i - 1]
            continue
        for j in range(i, len(odds), odds[i]):
            oddsum[j] += odds[i]
        if i == 0:
            continue
        oddsum[i] += oddsum[i - 1]
    return oddsum
sums = odd(1000000)
T = int(input())
for tc in range(1, T + 1):
    l, r = map(int, input().split())
    if l == 1:
        print('#{} {}'.format(tc, sums[r-1]))
    else:
        print('#{} {}'.format(tc, sums[r-1]-sums[l-2]))
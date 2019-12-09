import sys
sys.stdin = open('수.txt')

def xsis(k):
    c = 1
    while True:
        k -= c
        if k < 0:
            k += c
            break
        c += 1
    return k, c

T = int(input())
for tc in range(1, 3):
    p, q = list(map(int, input().split()))
    p, c = xsis(p)
    print(p, c)
    q, d = xsis(q)
    print(q, d)


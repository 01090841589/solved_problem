import sys
sys.stdin = open("소수.txt")

n = 1000000
a = [0, 0] + [1] * (n - 1)
primes = []
for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False
z = int(input())
for i in range(z):
    cnt = 0
    x, y = map(int, input().split())
    for j in primes:
        if x < j < y:
            cnt += j
    print('#%d %d' % (i + 1, cnt))
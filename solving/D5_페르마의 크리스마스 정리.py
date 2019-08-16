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
    if x <= 2:
        cnt = 1
    for j in primes:
        if x <= j <= y and j % 4 == 1:
            cnt += 1
    print('#%d %d' % (i + 1, cnt))
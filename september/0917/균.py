from decimal import Decimal

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    line = list(map(int, input().split()))
    X = line[:N]
    M = line[N:]
    ans = []
    for i in range(1, N):
        low = Decimal(X[i - 1])
        high = X[i]
        while high - low > Decimal(10) ** -12:
            mid = (low + high) / 2
            left = right = 0
            for i in range(N):
                force = M[i] / (mid - X[i]) ** 2
                if X[i] < mid:
                    left += force
                else:
                    right += force
            if left < right:
                high = mid
            else:
                low = mid
        ans.append(mid)
    print('#%s %s' % (tc, ' '.join('%.10f' % f for f in ans)))
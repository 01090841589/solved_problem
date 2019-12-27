import sys
sys.stdin = open("입국심사.txt")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    judge = []
    left, right = 0, 0
    for i in range(N):
        judge.append(int(input()))
        if right < judge[i]:
            right = judge[i]

    right *= K
    result = right
    while left <= right:
        mid = (left + right) // 2
        passed = 0
        for i in range(N):
            passed += mid // judge[i]
        if K <= passed:
            right = mid-1
            if result > mid:
                result = mid
        else:
            left = mid+1
    print('#{} {}'.format(tc, result))
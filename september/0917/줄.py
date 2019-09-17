import sys
sys.stdin = open("줄.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dp = [0 for _ in range(N + 1)]

    arr = list(map(int, input().split()))
    result = N

    for val in arr:
        #최장 증가 수열
        dp[val] = dp[val - 1] + 1
        #전체에서 감산
        result = min(result, N - dp[val])

    print('#{} {}'.format(tc, result))
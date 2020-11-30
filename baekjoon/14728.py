import sys
sys.stdin = open("14728.txt")

N,T = map(int, input().split())
problem = [0]+[list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(T+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1,T+1):
        if problem[i][0] <= j:
            if problem[i][1]+dp[i-1][j-problem[i][0]] > dp[i-1][j]:
                dp[i][j] = problem[i][1]+dp[i-1][j-problem[i][0]]

            else: dp[i][j] = dp[i-1][j]
        else: dp[i][j] =dp[i-1][j]

print(dp[N][T])

#
# for i in range(1,N+1):
#     for j in range(1,T+1):
#         if problem[i][0] <= j:
#             if problem[i][1]+dp[i-1][j-problem[i][0]] > dp[i-1][j]:
#                 dp[i][j] = problem[i][1]+dp[i-1][j-problem[i][0]]
#
#             else: dp[i][j] =dp[i-1][j]
#         else: dp[i][j] =dp[i-1][j]
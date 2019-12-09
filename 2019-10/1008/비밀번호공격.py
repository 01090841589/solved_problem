import sys
sys.stdin = open("비밀번호공격.txt")
#
# T = int(input())
# for tc in range(1, T+1):
#     M, N = map(int, input().split())
#     result = 0
#     passs = []
#     for i in range(1, M+1):
#         buf = i**N
#         combi = 1
#         buf *= combi
#         passs.append(buf)
#     result = passs[M-1]
#     for i in range(1, M):
#         combi = 1
#         for j in range(i):
#             combi *= (M-j)
#         for j in range(1, i+1):
#             combi //= j
#         print(combi)
#
#         result -= (passs[i-1]*combi)
#         passs[i] -= (passs[i-1]*combi)
#
#     print(passs)
#     print('#{} {}'.format(tc, result % 1000000007))

arr = [[0] * 101 for _ in range(101)]
for i in range(101):
    arr[1][i] = 1
    arr[i][0] = i


[print(arr[i]) for i in range(100)]
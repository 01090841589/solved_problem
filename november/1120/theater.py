import sys
sys.stdin = open("theater.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, R = map(int, input().split())







    # seat = [0]*100001
    # result = 0
    # N = int(input())
    # for i in range(N):
    #     a, b = map(int, input().split())
    #     for j in range(a, b+1):
    #         seat[j] = 1
    # for i in range(100001):
    #     if seat[i]:
    #         result += 1
    # print('#{} {}'.format(tc, result))

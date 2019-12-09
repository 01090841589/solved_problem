import sys
sys.stdin = open("입국심사.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    t = [int(input()) for _ in range(N)]
    cnt = 0
    waiting = [0] * N
    t.sort(reverse=True)
    print(t)
    while M > 1:
        if waiting.count(0):
            for i in range(N):
                if waiting[i] == 0:
                    waiting[i] = t[i]
                    M -= 1
        for i in range(N):
            waiting[i] -= 1
        cnt += 1
    while waiting.count(0) == 0:
        for i in range(N):
            waiting[i] -= 1
        cnt += 1
    k = waiting[-1] + t[-1]
    for i in range(N):

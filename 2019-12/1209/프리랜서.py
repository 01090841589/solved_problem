import sys
sys.stdin = open("프리랜서.txt")

def OPT(j, m, k):
    global result
    for i in range(j, N):
        if schedule[i][0] > m:
            if times[i] < schedule[i][2]+k:
                times[i] = schedule[i][2]+k
                OPT(i+1, schedule[i][1], schedule[i][2]+k)
    if result < k:
        result = k
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    schedule = [list(map(int, input().split())) for _ in range(N)]
    times = [0]*N
    schedule.sort(key=lambda k: k[1])
    for i in range(N):
        if times[i] < schedule[i][2]:
            OPT(i+1, schedule[i][1], schedule[i][2])
    print('#{} {}'.format(tc, result))
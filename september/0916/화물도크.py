import sys
sys.stdin = open("화물도크.txt")

def doke(k, visited, scr):
    global result
    if k == N:
        if result < scr:
            result = scr
        return
    if scr+(24-times[k][1]) <= result:
        return
    flag = 1
    for i in range(times[k][0],times[k][1]):
        if visited[i] != 0:
            flag = 0
            break
    if flag:
        visits = visited[:]
        for i in range(times[k][0], times[k][1]):
            visits[i] = 1
        doke(k+1, visits, scr+1)
    doke(k+1, visited, scr)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times = sorted(times, key=lambda times: times[1])
    # print(times)
    result = 0
    doke(0, [0]*24, 0)
    print('#{} {}'.format(tc, result))
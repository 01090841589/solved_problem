import sys
sys.stdin = open('일분배.txt')

def work_split(N, k, visited, per):
    global result
    if per <= result:
        return
    if N == k :
        if result < per:
            result = per
        return
    else:
        for i in range(N):
            if visited[i] == 1:
                continue
            visited[i] = 1
            work_split(N, k+1, visited, per*0.01*work[k][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    work_split(N, 0, [0]*N, 1)
    print('#%d %0.6f' % (tc, result*100))
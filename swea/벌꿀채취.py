import sys
sys.stdin = open("벌꿀채취.txt")

def gather(n, cnt, res):
    global MAX
    if n >= M:
        if MAX < res:
            MAX = res
        return
    if cnt+a[n] <= C:
        gather(n+1 ,cnt+a[n], res+(a[n]**2))
    gather(n+1 ,cnt, res)


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    box = []
    for i in range(N):
        for j in range(N-(M-1)):
            MAX = 0
            a = MAP[i][j:j+M]
            visited = [0]*M
            gather(0, 0, 0)
            box.append([MAX, i, j])
    box.sort(reverse=True)
    visited = [[0] * N for _ in range(N)]
    result = 0
    cnt = 0
    for a in range(len(box)-1):
        bee1 = [[box[a][1], box[a][2] + i] for i in range(M)]
        for b in range(1, len(box)):
            bee2 = [[box[b][1], box[b][2]+i] for i in range(M)]
            flag = 1
            for bb in bee2:
                if bb in bee1:
                    flag = 0
                    break
            if flag:
                if result < box[a][0]+box[b][0]:
                    result = box[a][0]+box[b][0]
    print('#{} {}'.format(tc, result))
import sys
sys.stdin = open('줄긋기.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dot = [list(map(int, input().split())) for _ in range(N)]
    ran = []
    for a in range(N-1):
        for b in range(a+1, N):
            if dot[a][1]-dot[b][1] == 0:
                if 'inf' not in ran:
                    ran.append('inf')
            else:
                K = (dot[a][0]-dot[b][0]) / (dot[a][1]-dot[b][1])
                if K not in ran:
                    ran.append(K)
    print('#{} {}'.format(tc, len(ran)))
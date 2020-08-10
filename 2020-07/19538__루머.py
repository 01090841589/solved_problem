import sys
sys.stdin = open("19538.txt")

N = int(input())
MAP = [[] for i in range(N+1)]
believe_cnt = [0] * (N+1)
for i in range(1, N+1):
    connect = list(map(int, input().split()))
    for j in range(len(connect)-1):
        MAP[i].append(connect[j])
        believe_cnt[i] = len(connect)-1
[print(MAP[i]) for i in range(N+1)]

spread_cnt = int(input())
spread = list(map(int, input().split()))

visited = [-1] * (N+1)
for i in range(spread_cnt):
    visited[spread[i]] = 0
print(visited)
print(believe_cnt)

for turn in range(1, 2):
    now_spread = spread[:]
    spreads = []
    next_spread = []

    for i in range(len(now_spread)):
        num = now_spread[i]
        if not MAP[num]:
            print(num)
            continue
        for j in MAP[num]:
            print(j)
            print(visited[j])
            if visited[j] == -1:
                print(j)
                belis = 0
                for k in MAP[j]:
                    if visited[k] > -1:
                        belis += 1
                print('bel', belis)
                if (len(MAP[j])+1)%2 >= belis:
                    spreads.append(j)
            else:
                pass
        
    next_spread = []
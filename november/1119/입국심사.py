import sys
sys.stdin = open("입국심사.txt")

def 입국심사(k):
    global result
    n = 0
    zeros = 0
    while True:
        flag = 0
        zeros = 0
        for i in range(N):
            if now[i] == 0:
                now[i] = judge[i]
                k -= 1
                flag = 1
        m = min(now)
        n += m
        for i in range(N):
            now[i] -= m
            if now[i] == 0:
                zeros += 1
        if k <= zeros:
            a = 0

            # for i in range(N):
            #     if a < now[i]+judge[i]:
            #         a = now[i]+judge[i]
            # for i in range(N):
            #     if k == 0:
            #         break
            #     if now[i]+judge[i] < a:
            #         now[i] += judge[i]
            #         k -= 1
            while True:
                if max(now) == 0:
                    k -= 1
                    now[i] += judge[i]
                for i in range(N):
                    if now[i]+judge[i] < max(now)+judge[now.index(max(now))]:
                        now[i] += judge[i]
                        now[now.index(max(now))] = 0
                        k -= 1
                        continue
                break
            result = n+max(now)
            return




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    judge = []
    now = [0] * N
    for _ in range(N):
        judge.append(int(input()))
    judge.sort()
    result = 0
    입국심사(M)
    print('#{} {}'.format(tc, result))
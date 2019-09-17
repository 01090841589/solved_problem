import sys
sys.stdin = open('pizza.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    bzip = []
    for c in range(len(data)):
        bzip.append(c+1)

    zzip = list(zip(data,bzip))

    oven = []
    flag = 0
    for i in range(M):
        a = data.pop(0)
        if len(oven) < N:
            oven.append(a)

        while len(oven) == N and oven.count(0) != 2 :
            for j in range(N):
                oven[j] //= 2
                if oven[j] < 1 and data :
                    oven[j] = data.pop(0)
            if oven.count(1)+oven.count(0) == 3:
                flag = 1
                break

        if flag:
            break
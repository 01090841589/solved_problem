import sys
sys.stdin = open('동환이.txt')

def buy(k, price, n):
    global result
    if k == N:
        if result > price+n:
            result = price+n
        return
    if price * (1 - (dis[k][1]*0.01)) < price:
        buy(k+1, price * (1 - (dis[k][1]*0.01)), n+dis[k][0])
    buy(k+1, price, n)
T = int(input())
for tc in range(1, T+1):
    N, C = map(int, input().split())
    result = C
    dis = [list(map(int, input().split())) for _ in range(N)]
    # dis.sort(reverse=True)
    visited = [0] * N
    buy(0, C, 0)
    print('#{} {}'.format(tc, result))
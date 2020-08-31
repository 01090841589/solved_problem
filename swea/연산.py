import sys
sys.stdin = open("연산.txt")

def multi(k, cnt):
    global result
    if result < cnt:
        return
    if k >= M:
        cnt += (k-M)//10
        cnt += (k-M)%10
        if result > cnt:
            result = cnt
        return
    multi(k*2, cnt+1)
    multi(k+1, cnt+1)




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 1000000
    multi(N, 0)
    # print('#{} {}'.format(tc, cnt))
    print(result)
import sys
sys.stdin = open("부분집합의합.txt")

def part_sum(k, cnt):
    global result
    a = sum(visit[k:N+1])+cnt
    if cnt > M:
        return
    if a < M:
        return
    if a == M:
        result += 1
        return
    if k == N+1:
        return
    part_sum(k+1, cnt+k)
    part_sum(k+1, cnt)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visit = [i for i in range(101)]
    result = 0
    part_sum(1, 0)
    print('#{} {}'.format(tc, result))

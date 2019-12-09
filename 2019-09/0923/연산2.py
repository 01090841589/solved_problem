import sys
sys.stdin = open('연산.txt')

from collections import deque

def BFS():
    global N, M, result, tc
    while Q:
        num, cnt = Q.popleft()
        if num == M:
            result = cnt
            return
        num2 = num + 1
        if 0 < num2 <= 1000000 and num_lst[num2] != 1:
            Q.append((num2, cnt+1))
            num_lst[num2] = 1
        num2 = num - 1
        if 0 < num2 <= 1000000 and num_lst[num2] != 1:
            Q.append((num2, cnt+1))
            num_lst[num2] = 1
        num2 = num*2
        if 0 < num2 <= 1000000 and num_lst[num2] != 1:
            Q.append((num2, cnt+1))
            num_lst[num2] = 1
        num2 = num - 10
        if 0 < num2 <= 1000000 and num_lst[num2] != 1:
            Q.append((num2, cnt+1))
            num_lst[num2] = 1

T = int(input())
for tc in range(1, T+1):
    num_lst = [0] * 1000001
    N, M = map(int, input().split())
    Q = deque()
    Q.append((N, 0))
    num_lst[N] = tc
    result = 0
    BFS()
    print('#{} {}'.format(tc, result))
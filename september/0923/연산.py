import sys
sys.stdin = open('연산.txt')


from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [990]*1000001
    visited[N] = 1
    stack = deque()
    stack.append(N)
    while stack:
        a = stack.popleft()
        if visited[a] = 1:
            continue
        if a == M:
            if visited[M] > visited[a]:
                visited[M] = visited[a]
            continue
        if a*2 < 1000000 and visited[a*2] > visited[a]:
            stack.append(a*2)
            visited[a*2] = visited[a]+1
            # if a < M//10:
            #     continue
        if a+1 < 1000000 and visited[a+1] > visited[a]:
            stack.append(a+1)
            visited[a+1] = visited[a]+1
        if 0 < a-1 and visited[a-1] > visited[a]:
            stack.append(a-1)
            visited[a-1] = visited[a]+1
        if 0 < a-10 and visited[a-10] > visited[a]:
            stack.append(a-10)
            visited[a-10] = visited[a]+1
    print('#{} {}'.format(tc, visited[M]-1))


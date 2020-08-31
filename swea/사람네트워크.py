import sys
sys.stdin = open("사람네트워크.txt")

from collections import deque
def search(k):
    stack = deque()
    stack.append(k)
    while stack:
        k = stack.popleft()
        for i in range(N):
            if node[k][i]:
                if visited[i]>0:
                    continue
                visited[i] = visited[k]+1
                stack.append(i)




T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    M = len(arr)-1
    K = []
    high = 0
    node = [[0]*(N+1) for _ in range(N)]
    result = 12312321
    for i in range(N):
        node[i] = arr[i*N+1:i*N+N+1]
    for i in range(N):
        if high < sum(node[i]):
            high = sum(node[i])
        K.append([i, sum(node[i])])
    for a in range(N):
        if K[a][1] < high-3:
            continue
        visited = [0] * N
        visited[a] = 1
        search(a)
        sums = sum(visited)-len(visited)
        if result > sums:
            result = sums
    print('#{} {}'.format(tc, result))
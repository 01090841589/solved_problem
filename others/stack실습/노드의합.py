import sys
sys.stdin = open('노드의합.txt')

def reverse_sum(n):
    tree[tree[n][2]][3] += tree[n][3]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(M)]
    tree = [[0] * 4 for _ in range(N+1)]
    for i in range(1, N+1):
        if i*2 <= N:
            tree[i][0] = i*2
        if i*2+1 <= N:
            tree[i][1] = i*2+1
        tree[i][2] = i//2
    for i in range(M):
        tree[node[i][0]][3] = node[i][1]
    for i in range(N, 1, -1):
        reverse_sum(i)
    print('#{} {}'.format(tc, tree[L][3]))
    node.reverse()
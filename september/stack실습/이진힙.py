import sys
sys.stdin = open('이진힙.txt')

def insert_tree(n):
    for i in range(1, N+1):
        if tree[i][3] == 0:
            tree[i][3] = n
            if i // 2 == 0:
                return
            while i > 1:
                if tree[i // 2][3] > tree[i][3]:
                    tree[i // 2][3] , tree[i][3] = tree[i][3] , tree[i//2][3]
                    i //= 2
                else:
                    return
            return


def node_sum(n):
    global result
    if n == 0:
        return
    result += tree[tree[n][2]][3]
    node_sum(tree[n][2])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0] * 4 for _ in range(N+1)]
    node = list(map(int, input().split()))
    result = 0
    for i in range(1, N+1):
        if i*2 <= N:
            tree[i][0] = i*2
        if i*2+1 <= N:
            tree[i][1] = i*2+1
        tree[i][2] = i//2
    for i in node:
        insert_tree(i)
    node_sum(N)
    print('#{} {}'.format(tc, result))
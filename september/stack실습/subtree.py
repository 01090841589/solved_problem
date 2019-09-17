import sys
sys.stdin = open('subtree.txt')

def deep(n):
    global result
    if tree[n][0] != 0:
        result += 1
        deep(tree[n][0])
    if tree[n][1] != 0:
        result += 1
        deep(tree[n][1])
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E + 2)]
    result = 1
    for i in range(len(node) // 2):
        if tree[node[2 * i]][0] == 0:
            tree[node[2 * i]][0] = node[2 * i + 1]
        else:
            tree[node[2 * i]][1] = node[2 * i + 1]
        tree[node[2 * i + 1]][2] = node[2 * i]
    deep(N)
    print('#{} {}'.format(tc, result))
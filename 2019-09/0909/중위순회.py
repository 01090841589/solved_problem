import sys
sys.stdin = open('중위순회.txt')

def mid(T):
    global result
    if T != 0:
        mid(tree[T][1])
        result += tree[T][0]
        mid(tree[T][2])


for tc in range(1, 11):
    N = int(input())
    node = [list(map(str, input().split())) for _ in range(N)]
    tree = [[0] * 4 for _ in range(N)]
    for i in range(N):
        tree[i][0] = node[i][1]
        if len(node[i]) > 2:
            tree[i][1] = int(node[i][2])
            tree[int(node[i][2])-1][3] = int(node[i][0])
        if len(node[i]) > 3:
            tree[i][2] = int(node[i][3])
            tree[int(node[i][3])-1][3] = int(node[i][0])
    tree.insert(0, [0]*4)
    result = ''
    mid(1)
    print('#{} {}'.format(tc, result))
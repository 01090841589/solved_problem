import sys
sys.stdin = open('완전이진탐색.txt')

def mid(T):
    global a
    if T != 0:
        mid(tree[T][0])
        tree[T][3] = a
        a += 1
        mid(tree[T][1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0] * 4 for _ in range(N+1)]
    a = 1
    for i in range(1, N+1):
        if i*2 <= N:
            tree[i][0] = i*2
        if i*2+1 <= N:
            tree[i][1] = i*2+1
        tree[i][2] = i//2
    mid(1)
    print('#{} {} {}'.format(tc, tree[1][3],tree[N//2][3]))

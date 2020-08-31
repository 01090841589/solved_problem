import sys
sys.stdin = open('공통조상.txt')

def front(T):
    global cnt
    if T != 0:
        cnt += 1
        front(tree[T][0])
        front(tree[T][1])


def parent(k, klist):
    if tree[k][2] != 0:
        klist.append(tree[k][2])
        parent(tree[k][2], klist)


T = int(input())
for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    node = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V+1)]
    # print(node)
    for i in range(E):
        tree[node[2*i+1]][2] = node[2*i]
        if tree[node[2*i]][0] == 0:
            tree[node[2*i]][0] = node[2*i+1]
        else:
            tree[node[2 * i]][1] = node[2 * i + 1]
    Alist = [A]
    parent(A, Alist)
    Blist = [B]
    parent(B, Blist)
    for i in Alist:
        if i in Blist:
            result = i
            break
    cnt = 0

    front(i)
    print('#{} {} {}'.format(tc, i, cnt))
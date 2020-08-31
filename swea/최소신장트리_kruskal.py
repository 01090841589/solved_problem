import sys
sys.stdin = open('최소신장트리.txt')

def go_parent(k):
    if visited[k] == k:
        return k
    else:
        return go_parent(visited[k])


def find_parent(a):
    if go_parent(a[0]) != go_parent(a[1]):
        return True
    else:
        return False


def change_child(a):
    i = go_parent(a[0])
    j = go_parent(a[1])
    if i < j:
        visited[j] = i
    else:
        visited[i] = j


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    MAP = [[0] * (V+1) for _ in range(V+1)]
    for c in node:
        MAP[c[0]][c[1]] = c[2]
        MAP[c[1]][c[0]] = c[2]
    visited = [i for i in range(V+1)]
    node.sort(key=lambda k: k[2])
    cnt = 0
    scr = 0
    for a in node:
        if cnt == V:
            break
        if find_parent(a):
            change_child(a)
            scr += a[2]
            cnt += 1

    print('#{} {}'.format(tc, scr))
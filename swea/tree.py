import sys
sys.stdin = open('tree.txt')

def front(T):
    if T != 0:
        print(T, end = ' ')
        front(tree[T][0])
        front(tree[T][1])
def mid(T):
    if T != 0:
        mid(tree[T][0])
        print(T, end = ' ')
        mid(tree[T][1])
def back(T):
    if T != 0:
        back(tree[T][0])
        back(tree[T][1])
        print(T, end = ' ')


N = int(input())
node = list(map(int, input().split()))
tree = [[0] * 3 for _ in range(N+1)]

for i in range(len(node)//2):
    if tree[node[2 * i]][0] == 0:
        tree[node[2 * i]][0] = node[2 * i + 1]
    else:
        tree[node[2 * i]][1] = node[2 * i + 1]
    tree[node[2 * i+1]][2] = node[2 * i]


[print(i, tree[i]) for i in range(N+1)]

#전위
print('전위순회:',end = ' ')
front(1)
print()
#중위
print('중위순회:',end = ' ')
mid(1)
print()
#후위
print('후위순회:',end = ' ')
back(1)

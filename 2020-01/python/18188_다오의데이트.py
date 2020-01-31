import sys
sys.stdin = open("다오의데이트.txt")

def go_dao(k, route):
    for i in range(4):
        if can[k][i]:


H, W = map(int, input().split())
print(H, W)
MAP = [list(input()) for _ in range(H)]
print(MAP)
A = int(input())
arr = ['W', 'A', 'S', 'D']
can = [[0, 0, 0, 0] for _ in range(A)]
for i in range(A):
    B, C = map(str, input().split())
    can[i][arr.index(B)] = 1
    can[i][arr.index(C)] = 1

go_dao(0, '')
print(can)
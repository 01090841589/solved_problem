import sys
sys.stdin = open("새로운게임.txt")

DIR = [[], [-1, 0], [0, 1], [1, 0], [0, -1]]
N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dron = [list(map(int, input().split())) for _ in range(K)]
print(MAP, dron)

for _ in range(K):
    for i in range(4):

        
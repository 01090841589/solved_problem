import sys
sys.stdin = open("새로운게임.txt")

N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dron = [list(map(int, input().split())) for _ in range(K)]
print(MAP, dron)
import sys
sys.stdin = open("갤러리.txt")

N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
print(MAP)
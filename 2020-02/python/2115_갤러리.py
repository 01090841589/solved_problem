import sys
sys.stdin = open("갤러리.txt")

N, M = map(int, input().split())
MAP = [map(int, input().split()) for _ in range(N)]
for i in range(N):
    pass
import sys
sys.stdin = open("폴짝게임.txt")

N, M, D = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]


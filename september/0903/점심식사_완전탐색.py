import sys
sys.stdin = open('점심식사.txt')

T = int(input())
for tc in range(1, 2):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    [print(MAP[i]) for i in range(N)]
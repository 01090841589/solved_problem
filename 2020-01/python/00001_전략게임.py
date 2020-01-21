import sys
sys.stdin = open("전략게임.txt")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    A, B, C = map(int, input().split())
    Acode = list(map(int, input().split()))
    Bcode = list(map(int, input().split()))
    Ccode = list(map(int, input().split()))
    code = []

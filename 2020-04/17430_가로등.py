import sys

sys.stdin = open("가로등.txt")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    road = [[0]*N for _ in range(N)]
    for i in range(N):
        a, b = map(int, input().split())





    print(road)
    
s
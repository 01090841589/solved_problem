import sys
sys.stdin = open("당근훔쳐먹기.txt")


N, T = map(int, input().split())
carrot = [[0, 0] for _ in range(N)]
for i in range(N):
    carrot[i][1], carrot[i][0] = map(int, input().split())
carrot.sort(reverse=True)
res = 0
for i in range(N):
    res += carrot[i][0] * (T-1-i) + carrot[i][1]
print(res)


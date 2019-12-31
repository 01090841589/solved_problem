import sys
sys.stdin = open("쉬운 계단 수.txt")
N = int(input())

numbers = [[0]*10 for _ in range(N)]
plus = [[[0]*3 for __ in range(10)] for _ in range(N)]
minus = [[[0]*3 for __ in range(10)] for _ in range(N)]

for i in range(1, 10):
    numbers[0][i] = 1
for i in range(N-1):
    for j in range(10):
        if j-1 >= 0:
            numbers[i+1][j-1] += numbers[i][j]
        if j+1 < 10:
            numbers[i+1][j+1] += numbers[i][j]
res = 0
for i in range(10):
    res += numbers[N-1][i]
print(res%1000000000)
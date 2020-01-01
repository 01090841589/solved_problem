import sys
sys.stdin = open("변형계단수.txt")
N = int(input())

numbers = [0]*10
plus = [[0]*2 for pl in range(10)]
minus = [[0]*2 for mi in range(10)]
plusbuf = [[0]*2 for plu in range(10)]
minusbuf = [[0]*2 for mn in range(10)]

for i in range(10):
    numbers[i] = 1
if N > 1:
    for i in range(10):
        if i+1 < 10:
            plus[i+1][0] += numbers[i]
        if i-1 >= 0:
            minus[i-1][0] += numbers[i]
for i in range(2, N):
    for k in range(1, -1, -1):
        for j in range(10):
            minusbuf[j][k] = minus[j][k]
            minus[j][k] = 0
            plusbuf[j][k] = plus[j][k]
            plus[j][k] = 0
    for k in range(1, -1, -1):
        for j in range(10):
            if j-1 >= 0:
                minus[j-1][0] += plusbuf[j][k]
                if k == 0:
                    minus[j-1][k+1] += minusbuf[j][k]
            if j+1 < 10:
                plus[j+1][0] += minusbuf[j][k]
                if k == 0:
                    plus[j+1][k+1] += plusbuf[j][k]
res = 0
if N == 1:
    res = 10
for i in range(10):
    for j in range(2):
        res += plus[i][j]
        res += minus[i][j]
print(res%1000000007)
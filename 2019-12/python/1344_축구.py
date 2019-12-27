import sys
sys.stdin = open("축구.txt")
N = int(input())
M = int(input())
A = [[0]*(i+1) for i in range(31)]
B = [[0]*(i+1) for i in range(31)]
A[0][0] = 1
B[0][0] = 1
for i in range(18):
    for j in range(i+1):
        A[i+1][j] += A[i][j]*(100-N)*0.01
        A[i+1][j+1] += A[i][j]*N*0.01
        B[i+1][j] += B[i][j]*(100-M)*0.01
        B[i+1][j+1] += B[i][j]*M*0.01
C = 0
D = 0
num = [2, 3, 5, 7, 11, 13, 17]
for i in num:
    C += A[18][i]
    D += B[18][i]
E = 1-(1-C)*(1-D)
print('%.10f' % (E))

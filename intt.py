import sys
sys.stdin = open("intt.txt")

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

input_num = int(input())
X = []
Y = []
delta = [1] * 3
for _ in range(input_num):
    y, x, att = map(str, input().split())
    y, x, att = float(y), float(x), int(att)
    X.append([1, y, x])
    Y.append(att)
output_num = int(input())
output = []
for _ in range(output_num):
    y, x = map(float, input().split())
    output.append([y, x])

# 1.
seta = 1
lamb = 0.1
dall = 10 ** -6
threshold = 0.5


# 2.
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# J 함수
def cost(seta, m):
    buf, buf2 = 0, 0
    for i in range(m):
        num = 0
        for j in range(3):
            num += X[i][j]*delta[j]
        buf += (-1)*(Y[i] * math.log(sigmoid(num)) - (1 - Y[i]) * math.log(1 - sigmoid(num)))
    for i in range(1, 3):
        buf2 += delta[i] ** 2

    return (1/m*buf) + (lamb/(2*m)*buf2)

def J(seta, m):
    buf = 0
    for i in range(m):
        num = 0
        for j in range(3):
            num += X[i][j]*delta[j]
        print(sigmoid(num))
        for j in range(3):
            buf += (sigmoid(num) - Y[j]) * X[j][0]

    print(1/m * (buf))
    return [1/m * (buf) + lamb/m*seta, 1/m * (buf)]

# buf -= (Y[i] * math.log(sigmoid(X[i])) - (1 - Y[i]) * math.log(1 - sigmoid(X[i])))

print(delta)
for _ in range(1):

    new_delta = [0] * 3
    new_delta[0] = delta[0] - J(delta[0], input_num)[1]
    for i in range(1, input_num):
        a = J(delta[i], input_num)
        new_delta[i] = delta[i] - a[0]
    delta = new_delta[:]
    print(_, delta)

    print(cost(delta[i], input_num))


for i in range(output_num):
    num = 0
    for j in range(2):
        num += output[i][j]*delta[j+1]
    print(num)
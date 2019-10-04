N = [1]*1001

N[0] = 0
N[1] = 0
for i in range(2, 1001):
    if N[i] == 1:
        for j in range(i+i, 1001, i):
            N[j] = 0
n = int(input())
num = list(map(int, input().split()))
result = 0
for i in num:
    if N[i] == 1:
        result += 1

print(result)
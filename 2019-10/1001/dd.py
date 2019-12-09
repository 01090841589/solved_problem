W = 10
n = 4
weight = [0, 5, 4, 6, 3]
value = [0, 10, 40, 30, 50]

K = [[0 for _ in range(50)] for _ in range(50)]

for i in range(n+1):
    for w in range(W+1):
        if weight[i] <= w:
            K[i][w] = max(value[i]+K[i-1][w-weight[i]], K[i-1][w])
        else :
            K[i][w] = K[i-1][w]
print(K[0])
print(K[1])
print(K[2])
print(K[3])
print(K[4])

ans = 0
print(K[4][10])
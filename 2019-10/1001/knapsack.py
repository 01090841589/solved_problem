def calcul(n, k, M, V):
    global ans
    if n == k:
        if ans < V:
            ans = V
        return
    if M+weight[k] < W:
        calcul(n, k+1, M+weight[k], V+value[k])
    calcul(n, k+1, M, V)



W = 10
n = 4
weight = [5, 4, 6, 3]
value = [10, 40, 30, 50]
A = [0] * n
ans = 0
visited = [0]*n
calcul(n, 0, 0, 0)
print("%d" %(ans))
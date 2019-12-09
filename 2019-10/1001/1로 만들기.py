def calcul(n, k):
    global result
    if result <= k:
        return
    if n == 1:
        if result > k:
            result = k
        return
    if n < 1:
        return
    if n % 3 == 0:
        calcul(n//3, k+1)
    if n % 2 == 0:
        calcul(n//2, k+1)
    calcul(n-1, k+1)

N = int(input())
result = 999999

calcul(N, 0)
print(result)
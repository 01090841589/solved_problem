
def coin(n):
    if n < 1:
        return 0
    return n * coin(n - 1) + (n // 2) * facto(n - 1)


def facto(n):
    if n == 0:
        return 0
    a = 1
    for i in range(n, 1, -1):
        a *= i
    return a

arr = [0 for _ in range(1001)]
print(arr)
for i in range(2, 1001):
    k = i * arr[i-1] + (i//2) * facto(i-1)
    arr[i] = k % 1000000007

b = 2
print(arr[20])
print(arr[22])
print(arr[23])
print(arr[24])
print(arr[25])
print(arr[26])
print(arr[27])
print(arr[28])
print(arr[29])
print(arr[30])
print(arr[110])
print(arr[1000])
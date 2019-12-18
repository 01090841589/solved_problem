def search(A, l, r, key):
    while (r - l > 1):
        m = l + (r - l) // 2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r
def LIS(A, size):
    MAP = [0 for i in range(size + 1)]
    len = 0
    MAP[0] = A[0]
    len = 1
    for i in range(1, size):
        if (A[i] < MAP[0]):
            MAP[0] = A[i]
        elif (A[i] > MAP[len - 1]):
            MAP[len] = A[i]
            len += 1
        else:
            MAP[search(MAP, -1, len - 1, A[i])] = A[i]
    return [len, MAP]
n = int(input())
A = list(map(int, input().split()))
res, arr = LIS(A, n)
print("{}".format(res))
for i in range(len(arr)):
    if arr[i] > 0:
        print("{}".format(arr[i]),end=" ")
    else:
        break
print()
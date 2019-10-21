A = [0] * 50000

a = 1
k = 1
for i in range(50000):
    A[i] = a
    a += k
for i in range(50000):
    print(A[i], end = ' ')
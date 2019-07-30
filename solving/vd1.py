N = [1, 2, 3]

right = []
left = []

def out(i, N):
    if sum(right) + i < sum(left):
        print('right')
    if sum(right) < sum(left)+i:
        left.append(i)
        N.remove(i)
        return N

M = N[:]

for i in N:
    out(i, M)
    print(M)
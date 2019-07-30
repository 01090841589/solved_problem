n = [4, 3, 2, 1]
right = []
left = []


for i, j in enumerate(n,1):
    print(i,j)
    if sum(left) < sum(right)+i:
        left.append(j)
    else:


        right.append(j)
    print(left)
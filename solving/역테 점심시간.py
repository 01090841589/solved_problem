T = 1
size = 5
mat = [
[0, 1, 1, 0, 0],
[0, 0, 1, 0, 3],
[0, 1, 0, 1, 0],
[0, 0, 0, 0, 0],
[1, 0, 5, 0, 0]
]
stair = []
for i in range(size):
    for j in range(size):
        if mat[i][j] > 1:
            stair.append([i, j, mat[i][j]])
print(stair)

def distance(size,c):
    for i in range(size):
        for j in range(size):
            if mat[i][j] == 1:
                for st in stair:
                    if (st[0]-i+) + (st[1]-i) + st[2] <= c:


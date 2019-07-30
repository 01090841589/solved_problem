T = 1
N = int(input())
mat = []
for a in range(N):
    mat.append(list(map(int,input().split())))
total = 0
def check_1(x):
    for Y in range(N):
        if mat_min[Y][x] == 1:
            return 5
            break
    return 9
def choose():
    for y in range(N):
        if mat_min[y].count(9) == 1:
            for x in range(N):
                if mat_min[y][x] == 9:
                    mat_min[y][x] = 1
mat_min_x = [0]*N
mat_min = []
for a in range(N):
    mat_min.append(mat_min_x[:])
for a in range(N):
    print(mat_min[a])
for y in range(N):
    for x in range(N):
        if mat[y][x] == min(mat[y]):
            mat_min[y][x] = 9
for a in range(N):
    print(mat_min[a])
choose()
for a in range(N):
    print(mat_min[a])
for check in range(N):
    for y in range(N):
        if mat_min[y].count(9) > 0:
            for x in range(N):
                if mat_min[y][x] == 9:
                    mat_min[y][x] = check_1(x)
for a in range(N):
    print(mat_min[a])
choose()
for a in range(N):
    print(mat_min[a])
for y in range(N):
    for x in range(N):
        if mat_min[y][x] == 1:
            total += mat[y][x]
print(total)
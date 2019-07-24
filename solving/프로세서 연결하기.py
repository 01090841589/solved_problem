location = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def length(y, x, i):
    cnt = 0
    while True:
        y = y + location[i][0]
        x = x + location[i][1]
        if 0 <= y < N and 0 <= x < N:
            if mat[y][x] == 0:  # 입력 C 와 다르게
                cnt += 1
            else:
                cnt = 0
                break
        else:
            if cnt == 0:
                cnt = 'x'
            break
    return cnt



mat2 = [[0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]]
N = len(mat)
print(len(mat))
for i in range(len(mat)):
    print(mat[i])

for i in range(len(mat)):
    for j in range(len(mat)):
        route = []
        if mat[i][j] == 1:
            for k in range(4):
                route.append(length(i,j,k))
            print(i,j,route)
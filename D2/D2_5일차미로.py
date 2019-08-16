DIR = [[0,1], [0,-1], [1, 0], [-1, 0]]
def maze(y, x):
    global result
    for arr in DIR:
        Y = y + arr[0]
        X = x + arr[1]
        if 0 <= X < n and 0 <= Y < n:
            if mat[Y][X] == 0:
                mat[Y][X] = 2
                maze(Y, X)
            elif mat[Y][X] == 3:
                result = 1
                return
T = int(input())
for test_case in range(1, T+1):
    result = 0
    mat = []
    n = int(input())
    for i in range(n):
        mat.append(list(map(int,list(input()))))
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 2:
                y, x = i, j
    maze(y, x)
    print('#{} {}'.format(test_case,result))
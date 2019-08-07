for test_case in range(1, 11):
    T = input()
    max_num = 0
    mat = []
    for i in range(100):
        mat.append(list(map(int,input().split())))

    for i in range(100):
        sum = 0
        for j in range(100):
            sum += mat[i][j]
        if sum > max_num:
            max_num = sum
    for j in range(100):
        sum = 0
        for i in range(100):
            sum += mat[i][j]
        if sum > max_num:
            max_num = sum
    sum = 0
    for i in range(100):
        sum += mat[i][i]
    if sum > max_num:
        max_num = sum
    sum = 0
    for i in range(100):
        sum += mat[99-i][i]
    if sum > max_num:
        max_num = sum
    print('#{} {}'.format(test_case,max_num))
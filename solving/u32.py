T = 10
N = 5
K = 1
max_num = 0
max_locate = []
route = [[9, 3, 2, 3, 2], [6, 3, 1, 7, 5], [3, 4, 8, 9, 9], [2, 3, 7, 7, 7], [7, 6, 5, 5, 8]]
for i in range(len(route)):
    if max(route[i]) > max_num:
        max_num = max(route[i])
    print(route[i])
for i in range(len(route)):
    for j in range(len(route)):
        if route[i][j] == max_num:
            max_locate.append([i, j])
print(max_num, max_locate)

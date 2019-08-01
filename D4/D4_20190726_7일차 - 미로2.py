DIR = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def check_route(y, x, k):
    y += DIR[k][0]
    x += DIR[k][1]
    cnt = 0
    if 0 < x < 99 and 0 < y < 99:
        if maze[y][x] == 0:
            maze[y][x] = 9
            cnt = 1
        elif maze[y][x] == 3:
            cnt = 2
    return cnt

for test_case in range(1,11):
    T = int(input())
    maze = []
    for mazey in range(100):
        mazex = []
        inp = input()
        for mazx in range(100):
            mazex.append(int(inp[mazx]))
        maze.append(mazex)
    dup_route = []
    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                dup_route.append([i, j])
    cnt = 0
    while cnt < 2:
        route_result = []
        for X in dup_route:
            for arrow in range(4):
                cnt = check_route(X[0], X[1], arrow)
                if cnt == 1:
                    route_result.append([X[0]+DIR[arrow][0], X[1]+DIR[arrow][1]])
                elif cnt == 2:
                    print('#{0} 1'.format(test_case))
                    break
            if cnt == 2:
                break
        if cnt == 2:
            break
        if len(route_result) == 0:
            cnt = 3
            print('#{0} 0'.format(test_case))
            break
        dup_route = route_result[:]
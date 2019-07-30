DIR = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
T = int(input())
for test_case in range(1,T+1):
    N = []
    n = int(input())
    for nu in range(n):
        xsis = []
        a = input()
        for A in a:
            if A == '.':
                xsis.append(0)
            else:
                xsis.append(9)
        N.append(xsis)

    def search_bom(x, y):
        cnt = 0
        if N[y][x] == 0:
            for c in DIR:
                Y = y+c[0]
                X = x+c[1]
                if 0 <= Y < len(N) and 0 <= X < len(N):
                    if N[Y][X] == 9:
                        cnt += 1
        else :
            cnt = 9
        return cnt
    def zero(x, y, click):
        if N[y][x] == 0:
            N[y][x] = 10
            for c in DIR:
                Y = y+c[0]
                X = x+c[1]
                if 0 <= Y < len(N) and 0 <= X < len(N):
                    if N[Y][X] != 0:
                        N[Y][X] = 10
                    else:
                        a = X
                        b = Y
                        zero(a,b,click)
        return click
    click = 0
    for x in range(len(N)):
        for y in range(len(N)):
            N[y][x] = search_bom(x, y)
    for x in range(len(N)):
        for y in range(len(N)):
            if N[y][x] == 0:
                click += 1
            click = zero(x, y,click)
    for x in range(len(N)):
        for y in range(len(N)):
            if N[y][x] < 9:
                click += 1
    print('#{0} {1}'.format(test_case,click))

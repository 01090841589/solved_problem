DIR = [[0, -1], [0, 1], [-1, 0]]
def find_ladder(x, y):
    for arr in DIR:
        X = x+arr[1]
        Y = y+arr[0]
        if 0 <= X < 100 and 0 <= Y < 100:
            if ladder[Y][X] == 1:
                ladder[Y][X] = 2
                a = X
                b = Y
                return find_ladder(a, b)
T = 10
for test_case in range(10):
    t = int(input())
    ladder = []
    for i in range(100):
        ladder_x = list(map(int,input().split()))
        ladder.append(ladder_x)
    for i in range(100):
        if ladder[99][i] == 2:
            x = i
            y = 99
    find_ladder(x, y)

    for i in range(100):
        if ladder[0][i] == 2:
            print('#{0} {1}'.format(t,i))
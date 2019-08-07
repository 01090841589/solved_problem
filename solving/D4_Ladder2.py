DIR = [[0, -1], [0, 1], [-1, 0]]
min_path = 200
def find_ladder(x, y, c):
    for arr in DIR:
        X = x+arr[1]
        Y = y+arr[0]
        if Y == 0:
            print(c)
            return c
        if 0 <= X < 100 and 1 <= Y < 100:
            if ladder[Y][X] == 1:
                a = X
                b = Y
                return find_ladder(a, b, c+1)
for test_case in range(10):
    t = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int,input().strip().split())))
    for i in range(100):
        if ladder[99][i] == 1:
            x = i
            y = 99
            C = find_ladder(x, y, 1)
            if C != None and C < min_path:
                min_path = C
                print(C)
    for i in range(100):
        if ladder[0][i] == 2:
            print('#{0} {1}'.format(t,i))\
            

import sys
sys.stdin = open('미로2.txt')

DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def mage(stack):
    global result
    while stack:
        [y, x] = stack.pop()
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= X < 100 and 0 <= Y < 100:
                if MAP[Y][X] == 0:
                    MAP[Y][X] = 2
                    stack.append([Y, X])
                elif MAP[Y][X] == 3:
                    result = 1
                    return


for i in range(1, 11):
    T = int(input())
    MAP = [list(map(int, input())) for _ in range(100)]
    result = 0
    mage([[1, 1]])
    print(result)
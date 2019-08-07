DIR = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
def turn(y, x, c):
    cnt = 0
    game[y][x] = c
    for arr in DIR:
        Y = y
        X = x
        cnt = 0
        while True:
            Y += arr[0]
            X += arr[1]
            if 0 <= X < NM[0] and 0 <= Y < NM[0]:
                if game[Y][X] != c and game[Y][X] != 0:
                    cnt += 1
                elif game[Y][X] == c:
                    for change in range(cnt):
                        Y -= arr[0]
                        X -= arr[1]
                        if 0 <= X < NM[0] and 0 <= Y < NM[0]:
                            game[Y][X] = c
                    break
                else :
                    break
            else:
                break
T = int(input())
for test_case in range(1, T+1):
    NM = list(map(int,input().split()))
    game = []
    black = 0
    white = 0
    for i in range(NM[0]):
        game.append([0]*NM[0])
    game[NM[0]//2-1][NM[0]//2-1] = 2
    game[NM[0]//2-1][NM[0]//2] = 1
    game[NM[0]//2][NM[0]//2-1] = 1
    game[NM[0]//2][NM[0]//2] = 2
    for i in range(NM[1]):
        x, y, c =map(int,input().split())
        turn(y-1, x-1, c)
    for i in range(NM[0]):
        black += game[i].count(1)
        white += game[i].count(2)
    print('#{} {} {}'.format(test_case,black, white))
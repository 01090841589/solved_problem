def game_start(board):
    game = []
    for i in range(board):
        xsite = []
        for j in range(board):
            xsite.append(0)
        game.append(xsite)
    for i in range(board//2-1,board//2+1):
        for j in range(board//2-1,board//2+1):
            if i == j :
                game[i][j] = 2
            else :
                game[i][j] = 1
    return game
T = int(input())
for test_case in range(1,T+1):
    NM = input().split()
    NM = list(map(int,NM))
    board = NM[0]
    M = NM[1]
    game = game_start(board)
    for order in range(M):
        pick = input().split(' ')
        pick = list(map(int,pick))
        x = pick[1]-1
        y = pick[0]-1
        game[y][x] = pick[2]
        for x_val in range(x-1, x+2):
            for y_val in range(y-1, y+2):
                if 0 <= x_val < board and 0 <= y_val < board:
                        if game[y_val][x_val] != 0:
                            if (y_val != y) or (x_val != x):
                                move = [y_val-y,x_val-x]
                                x_move, y_move = x_val, y_val
                                while game[y_move][x_move] != 0:
                                    if move[1] != 0 and move[0] == 0 and 0 < x_move < board-1:
                                        if game[y_move][x_move+move[1]] != 0:
                                            x_move += move[1]
                                        else :
                                            break
                                    elif move[0] != 0 and move[1] == 0 and 0 < y_move < board-1:
                                        if game[y_move+move[0]][x_move] != 0:
                                            y_move += move[0]
                                        else :
                                            break
                                    elif move[0] != 0 and move[1] != 0 and 0 < x_move < board-1 and 0 < y_move < board-1:
                                        if x_move == board-1 or y_move == board-1:
                                            break
                                        elif game[y_move+move[0]][x_move+move[1]] != 0:
                                            x_move += move[1]
                                            y_move += move[0]
                                        else :
                                            break
                                    else :
                                        break
                                while y_move != y_val or x_move != x_val:
                                    if game[y_move][x_move] == game[y][x]:
                                        while y_move != y or x_move != x:
                                            y_move -= move[0]
                                            x_move -= move[1]
                                            game[y_move][x_move] = pick[2]
                                        break
                                    y_move -= move[0]
                                    x_move -= move[1]
        black = 0
        white = 0
        for a in range(board):
            print(game[a])
        for a in range(board):
            for b in range(board):
                if game[a][b] == 1:
                    black += 1
                elif game[a][b] == 2:
                    white += 1
    print('#{0} {1} {2}'.format(test_case,black, white))
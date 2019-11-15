
def find(y, x, k, N, board, result):
    if board[y][x] == 0:
        return result
    if k == 0:
        if y+1 < N and x+2 < N:
            num = board[y][x]
            if board[y+1][x] == num and board[y+1][x+1] == num and board[y+1][x+2] == num:
                if board[y][x+1] == 0 and board[y][x+2] == 0:
                    board[y + 1][x] = 0
                    board[y + 1][x+1] = 0
                    board[y + 1][x+2] = 0
                    board[y][x] = 0
                    return result+1
    elif k == 1:
        if x+2 < N:
            num = board[y][x]
            if board[y][x+1] == num and board[y][x+2] == num and board[y-1][x+2] == num:
                if board[y-1][x] == 0 and board[y-1][x+1] == 0:
                    board[y][x] = 0
                    board[y][x + 1] = 0
                    board[y][x + 2] = 0
                    board[y-1][x + 2] = 0
                    return result + 1
                elif board[y-1][x] == 0 and board[y-1][x+2] == 0:
                    board[y][x] = 0
                    board[y][x + 1] = 0
                    board[y][x + 2] = 0
                    board[y-1][x + 1] = 0
                    return result + 1
    elif k == 2:
        if x+1 < N:
            num = board[y][x]
            if board[y][x+1] == num and board[y - 1][x+1] == num and board[y - 2][x + 1] == num:
                if board[y-1][x] == 0 and board[y-2][x] == 0:
                    board[y][x] = 0
                    board[y][x+1] = 0
                    board[y-1][x+1] = 0
                    board[y-2][x+1] = 0
                    return result + 1



    elif k == 3:
        if y+2 < N and x+1 <N:
            num = board[y][x]
            if board[y+1][x] == num and board[y+2][x] == num and board[y+2][x+1] == num:
                if board[y][x+1] == 0 and board[y+1][x+1] == 0:
                    board[y][x] = 0
                    board[y+1][x] = 0
                    board[y+2][x] = 0
                    board[y+2][x+1] = 0
                    return result + 1


    return result
def solution(board):
    N = len(board)
    result = 0
    [print(board[i]) for i in range(N)]
    while True:
        flag = 0
        for x in range(N):
            if flag:
                break
            for y in range(N):
                if board[y][x] > 0:
                    result = find(y, x, 0, N, board, result)
                    if board[y][x] == 0:
                        flag = 1
                    result = find(y, x, 1, N, board, result)
                    if board[y][x] == 0:
                        flag = 1
                    result = find(y, x, 2, N, board, result)
                    if board[y][x] == 0:
                        flag = 1
                    result = find(y, x, 3, N, board, result)
                    break
        if x == N-1:
            break
    answer = result
    return answer


print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))
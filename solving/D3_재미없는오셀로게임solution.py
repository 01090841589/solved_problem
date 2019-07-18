DIR = ((1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1))
black_white = [1, 2]


def check(y, x, c, i):
    global n
    cnt = 0
    while True:
        y = y + DIR[i][0]
        x = x + DIR[i][1]
        if y >= 0 and y < n and x >= 0 and x < n:
            if board[y][x] == black_white[c % 2]:  # 입력 C 와 다르게
                cnt += 1
            elif board[y][x] == black_white[(c + 1) % 2]:  # 입력 C와 같다면
                for _ in range(cnt):
                    y = y - DIR[i][0]
                    x = x - DIR[i][1]
                    board[y][x] = black_white[(c + 1) % 2]
                break
            elif board[y][x] == 0:
                break
        else:
            break



for t in range(int(input())):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    mid = n // 2
    board[mid - 1][mid] = 1
    board[mid - 1][mid - 1] = 2
    board[mid][mid - 1] = 1
    board[mid][mid] = 2
    for i in range(m):
        y, x, c = map(int, input().split())
        y = y - 1
        x = x - 1
        board[y][x] = c
        for j in range(8):
            check(y, x, c, j)
        for a in range(n):
            print(board[a])
    num_w = num_b = 0
    for i in board:
        num_b += i.count(1)
        num_w += i.count(2)
    print("#{} {} {}".format(t + 1, num_b, num_w))
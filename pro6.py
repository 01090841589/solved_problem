from itertools import permutations
def solution(board, r, c):
    answer = 0
    max_num = 0
    for y in range(4):
        for x in range(4):
            if board[y][x]:
                if max_num < board[y][x]:
                    max_num = board[y][x]
    scr = 999999
    sites = [[] for _ in range(max_num)]
    for ords in permutations(range(max_num), max_num):
        for i in range(2**max_num):
            print(i)
            for j in range(max_num):
                if i & (1<<j):
                    print("오른쪽")
                else:
                    print("왼쪽")


    return answer





solution([[1,4,4,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)
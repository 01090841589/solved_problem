import sys
sys.stdin = open("최소합.txt")


DIR = [[0, 1], [1, 0]]
def search_num(y, x, total):
    global result
    if total >= result:
        return
    if x == n-1 and y == n-1:
        if total < result:
            result = total
    for c in DIR:
        Y = y + c[0]
        X = x + c[1]
        if 0 <= X < n and 0 <= Y < n:
            search_num(Y, X, total+mat[Y][X])

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    result = 9 * n
    mat = [list(map(int, input().split())) for _ in range(n)]
    search_num(0, 0, mat[0][0])

    print("#{} {}".format(test_case, result))
import sys
sys.stdin = open('콩.txt')

DIR = [[0, 2], [2, 0], [0, -2], [-2, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    result = 0
    for a in range(4):
        mat = [[0] * N for _ in range(M)]
        for i in range(M):
            cnt = (a + i) % 4
            for j in range(N):
                if cnt > 1:
                    mat[i][j] = 1
                    cnt -= 1
                else:
                    cnt = (cnt - 1) % 4
        total = [mat[i].count(1) for i in range(M)]
        if result < sum(total):
            result = sum(total)
    [print(mat[i]) for i in range(M)]
    print('#{} {}'.format(test_case, result))
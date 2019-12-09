import sys
sys.stdin = open("숫자만들기.txt")


opera = ['0', '1', '2', '3']
T = int(input())
for tc in range(1, 2):
    N = int(input())
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    operation = []
    sums = 0
    for i in range(4):
        if op[i] > 1:
            sums += op[i]-1
    for a in range(4):
        operation.extend([opera[a]] * op[a])
    MAX = -100000000
    MIN = 100000000
    visited = [0] * (N-1)

    print('#{} {}'.format(tc, MAX-MIN))
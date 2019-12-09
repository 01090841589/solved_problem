import sys
sys.stdin = open("숫자.txt")


def calcul(k, ops, scr):
    global low, high
    if k == N:
        if low > scr:
            low = scr
        if high < scr:
            high = scr
        return
    for i in range(4):
        if ops[i] > 0 and i == 0:
            ops[i] -= 1
            calcul(k+1, ops[:], scr+nums[k+1])
            ops[i] += 1
        if ops[i] > 0 and i == 1:
            ops[i] -= 1
            calcul(k+1, ops[:], scr-nums[k+1])
            ops[i] += 1
        if ops[i] > 0 and i == 2:
            ops[i] -= 1
            calcul(k+1, ops[:], scr*nums[k+1])
            ops[i] += 1
        if ops[i] > 0 and i == 3:
            ops[i] -= 1
            calcul(k+1, ops[:], int(scr/nums[k+1]))
            ops[i] += 1



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N -= 1
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    opera = []
    a = 0
    low, high = 999999, -999999
    for i in range(len(op)):
        if i == 0:
            for j in range(op[i]):
                opera.append('+')
        if i == 1:
            for j in range(op[i]):
                opera.append('-')
        if i == 2:
            for j in range(op[i]):
                opera.append('*')
        if i == 3:
            for j in range(op[i]):
                opera.append('/')
    calcul(0, op[:], nums[0])
    print('#{} {}'.format(tc, high-low))
import sys
sys.stdin = open("숫자.txt")


def permu(k):
    global low, high, a
    a += 1
    if k == N:
        scr = nums[0]
        for i in range(N):
            if opera[i] == '+':
                scr = scr + nums[i+1]
            elif opera[i] == '-':
                scr = scr - nums[i + 1]
            elif opera[i] == '*':
                scr = scr * nums[i + 1]
            elif opera[i] == '/':
                scr = int(scr / nums[i + 1])
        if low > scr:
            low = scr
        if high < scr:
            high = scr
        return
    buf = 0
    for i in range(k, N):
        if opera[i] == opera[k] and i != k:
            continue
        opera[i], opera[k] = opera[k], opera[i]
        permu(k+1+buf)
        opera[i], opera[k] = opera[k], opera[i]


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
    # print(opera)
    permu(0)
    print('#{} {}'.format(tc, high-low))
import sys
sys.stdin = open("이진수2.txt")

T = int(input())
for tc in range(1, T+1):
    n = float(input())

    num = 0.5
    result = ''
    while True:
        if n >= num:
            n -= num
            result += '1'
        else:
            result += '0'
        num /= 2
        if n == 0:
            print('#{} {}'.format(tc, result))
            break
        if len(result) > 12:
            print('#{} overflow'.format(tc))
            break
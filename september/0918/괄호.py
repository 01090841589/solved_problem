import sys
sys.stdin = open("괄호.txt")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    i = 1
    N -= 1
    cnt = 0
    while True:
        if N - i < 0 :
            break
        N = N-i
        i += 1
    lst = [')'] + ['(']
    i -= 1
    lst += [')'] * i + ['('] * i
    for i in range(N):
        lst[i+1], lst[i+2] = lst[i+2], lst[i+1]
    print('#{} {}'.format(tc, ''.join(lst)))

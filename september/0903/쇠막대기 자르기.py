import sys
sys.stdin = open('쇠막대기.txt')


T = int(input())
for tc in range(1, T+1):
    stick = list(map(str, input()))
    print(stick)
    total = 0
    cnt = stick.count('(')
    depth = 0
    for i in range(len(stick)):
        print(depth, end = ' ')
        if stick[i] == '(':
            depth += 1
        elif stick[i] == ')':
            if stick[i-1] == '(':
                cnt -= 1
                depth -= 1
                total += depth
            else:
                depth -= 1
    print('{} {}'.format(tc, total + cnt))
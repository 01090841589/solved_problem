T = int(input())
for test_case in range(1, T+1):
    inp = input().split(' ')
    inp = list(map(int,inp))
    A, B, C = inp[0], inp[1], inp[2]
    a = C//A
    b = C//B
    if a > b :
        print('#{0} {1}'.format(test_case, a))
    else:
        print('#{0} {1}'.format(test_case, b))
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    print('#{}'.format(test_case),end='')
    for i in range(N):
        print(' 1/{}'.format(N),end='')
    print()
T = int(input())
for test_case in range(1, T+1):
    inp = input().split(' ')
    inp = list(map(int,inp))
    if inp[2] < inp[0] :
        print('#{0} {1}'.format(test_case,inp[0]-inp[2]))
    elif inp[0] <= inp[2] <= inp[1] :
        print('#{0} {1}'.format(test_case,0))
    else :
        print('#{0} {1}'.format(test_case,-1))
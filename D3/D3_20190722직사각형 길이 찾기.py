T = int(input())
for test_case in range(1, T+1):
    length = input().split(' ')
    length = list(map(int,length))
    print(len)
    comp1 = length[0]
    if length[1] != length[0]:
        comp2 = length[1]
        if length[2] != length[0]:
            print('#{0} {1}'.format(test_case, length[0]))
        else :
            print('#{0} {1}'.format(test_case,length[1]))
    else :
        print('#{0} {1}'.format(test_case,length[2]))
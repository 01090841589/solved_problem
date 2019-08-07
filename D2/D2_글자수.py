T = int(input())
for test_case in range(1, T+1):
    N  = int(input())
    total = 0
    for i in range(10, N + 10, 10):
        if i == 10:
            total = 1
        elif (i // 10) % 2:
            total = 2*total-1
        else :
            total = 2*total+1
    print('#{} {}'.format(test_case,total))
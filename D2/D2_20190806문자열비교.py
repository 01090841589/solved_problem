T = int(input())
for test_case in range(1, T+1):
    A = input()
    B = input()
    if A in B:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))
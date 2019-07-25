T = int(input())
for test_case in range(1, T+1):
    num = int(input())
    if num % 2 == 1 :
        print('#{0} {1}'.format(test_case,'Odd'))
    else:
        print('#{0} {1}'.format(test_case,'Even'))
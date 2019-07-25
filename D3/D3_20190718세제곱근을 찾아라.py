import math

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    N3 = N ** (1/3)
    if math.isclose(N3, round(N3)):
        print('#{0} {1}'.format(test_case, round(N3)))
    else :
        print('#{0} -1'.format(test_case))
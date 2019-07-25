T = int(input())
for test_case in range(1,T+1):
    N = list(map(int,input().split()))
    total = 0
    for i in range(1,(N[0]//N[1])+1):
        total += (2*i)-1
    print('#{0} {1}'.format(test_case,total))

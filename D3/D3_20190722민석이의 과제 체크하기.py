T = int(input())
for test_case in range(1,T+1):
    TC = input().split(' ')
    TC = list(map(int,TC))
    K = TC[1]
    N = []
    for a in range(1, TC[0] + 1):
        N.append(a)
    submit = input().split(' ')
    submit = list(map(int,submit))
    for i in range(len(submit)):
        N.remove(submit[i])
    print('#{0}'.format(test_case),end=' ')
    for i in range(len(N)):
        print(N[i],end=' ')
    print()
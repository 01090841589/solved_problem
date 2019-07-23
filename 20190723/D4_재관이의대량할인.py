T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    Ci = list(map(int,input().split()))
    Ci.sort()
    total = 0
    for i in range(0,len(Ci)//3):
        total += Ci.pop()
        total += Ci.pop()
        Ci.pop()
    print('#{0} {1}'.format(test_case,total+sum(Ci)))
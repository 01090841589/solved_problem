def Neuma(a, b, f, A, B, F):
    dis = b-a
    a = a+A*dis/(B+F)
    b = b-B*dis/(B+F)
    f = f+F*dis/(B+F)
    dis = b-a
    a = a+A*dis/(A+F)
    b = b-B*dis/(A+F)
    f = f+F*dis/(A+F)
    return a, b, f

T = int(input())
for test_case in range(1,T+1):
    DABF = input().split(' ')
    DABF = list(map(int,DABF))
    b, A, B, F = DABF[0], DABF[1], DABF[2], DABF[3]
    a = 0
    f = 0
    for i in range(100):
        a, b, f = Neuma(a, b, f, A, B, F)

    print('#{0} {1}'.format(test_case, f))
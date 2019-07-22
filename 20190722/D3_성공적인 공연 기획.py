T = int(input())
for test_case in range(1, T+1):
    crow = input()
    ancore = 0
    first_ancore = 0
    for i in range(len(crow)):
        if crow[i] == '0':
            first_ancore += 1
        else :
            break
    crow = int(crow)
    while crow % 10 != 0:
        crow //= 10
    while crow != 0:
        if crow % 10 == 0:
            ancore += 1
        else :
            ancore -= (crow % 10)-1
            if ancore < 0 :
                ancore = 0
        crow //= 10
    print('#{0} {1}'.format(test_case,ancore+first_ancore))
result = []
T = int(input())
for test_case in range(1, T+1):
    score = list(map(int,input().split()))
    if (score[0] / score[1]) < (score[2] / score[3]):
        result.append('BOB')
    elif (score[0] / score[1]) > (score[2] / score[3]):
        result.append('ALICE')
    else:
        result.append('DRAW')
for i in range(T):
    print('#{0} {1}'.format(i+1, result[i]))

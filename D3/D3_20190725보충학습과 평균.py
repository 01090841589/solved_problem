T = int(input())
for test_case in range(1, T+1):
    score = list(map(int,input().split()))
    for i in range(len(score)):
        if score[i] < 40:
            score[i] = 40
    print('#{0} {1}'.format(test_case,round(sum(score)/len(score))))
T = int(input())
for test_case in range(1,T+1):
    NK = input().split(' ')
    N, K = int(NK[0]), int(NK[1])
    score = input().split(' ')
    score = list(map(int,score))
    score.sort(reverse=True)

    total = 0
    for i in range(K):
        total += score[i]
    print('#{0} {1}'.format(test_case,total))
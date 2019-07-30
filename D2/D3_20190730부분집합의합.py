from itertools import combinations
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for test_case in range(1, T+1):
    cnt =0
    NK = list(map(int,input().split()))
    for a in combinations(A,NK[0]):
        if sum(a) == NK[1]:
            cnt += 1
    print('#{0} {1}'.format(test_case,cnt))
for test_case in range(1,11):
    N = int(input())
    num = list(map(int,input().split()))
    for i in range(N):
        num[num.index(max(num))] -= 1
        num[num.index(min(num))] += 1
    print('#{} {}'.format(test_case, max(num) - min(num)))
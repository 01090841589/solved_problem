T = int(input())
for test_case in range(1, T+1):
    N, M, L = map(int,input().split())
    nums = list(map(int,input().split()))

    num_plus = []
    [num_plus.append(list(map(int,input().split()))) for _ in range(M)]
    for plus in num_plus:
        nums.insert(plus[0],plus[1])
    print('#{} {}'.format(test_case, nums[L]))
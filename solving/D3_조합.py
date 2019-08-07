T = int(input())
for test_case in range(1, T+1):
    NR = list(map(int, input().split()))
    total = 1
    NR[1] = min(NR[1], NR[0]-NR[1])
    for i in range(NR[1]):
        total *= NR[0]-i
        total //= i+1
    print('#{} {}'.format(test_case,total%1234567891))
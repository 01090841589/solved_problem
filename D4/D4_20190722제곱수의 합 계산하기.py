T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    si = input().split()
    si = list(map(int,si))
    total = 0
    for i in range(len(si)):
        total += (si[i]//10) ** (si[i]%10)
    print('#{0} {1}'.format(test_case,total))
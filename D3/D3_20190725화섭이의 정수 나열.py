T = int(input())
for test_case in range(1, T+1):
    number = ''
    N = int(input())
    while len(number) < N:
        num = input().split()
        num = ''.join(num)
        number += num
    for i in range(1000):
        if str(i) not in number:
            print('#{0} {1}'.format(test_case,i))
            break
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n = input()
    num = []
    for i in range(10):
        num.append(n.count(str(i)))
    num = list(map(int,num))
    for i in range(9,-1,-1):
        if num[i] == max(num):
            print('#{0} {1} {2}'.format(test_case,i,max(num)))
            break
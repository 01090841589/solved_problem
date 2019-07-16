T = int(input())
for i in range(T) :
    N = int(input())
    num = input().split(' ')
    num = list(map(int,num))
    num.sort()
    print('#{0}'.format(i+1),end=' ')
    for j in range(len(num)) :
        print('{0}'.format(num[j]),end=' ')
    print('')
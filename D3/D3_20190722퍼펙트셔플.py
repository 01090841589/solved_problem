T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    word = input().split(' ')
    word = [x for x in word if x]
    print('#{0}'.format(test_case),end=' ')
    if len(word) % 2:
        for i in range(N//2):
            print(word[i],end=' ')
            print(word[N//2+i+1],end=' ')
        print(word[i+1])
    else :
        for i in range(N//2):
            print(word[i],end=' ')
            print(word[N//2+i],end=' ')
        print('')
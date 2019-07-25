T = int(input())
for test_case in range(1, T+1):
    word = input()
    H = int(input())
    location = input().split(' ')
    location = list(map(int,location))
    for hypn in range(len(word)+1):
        if hypn == 0:
            cal_hypn = [0]
        else :
            cal_hypn.append(0)
    for i in location:
        cal_hypn[i] += 1
    print('#{0} '.format(test_case),end='')
    for j in range(len(word)):
        print('-' * cal_hypn[j]+word[j],end='')
    print('-' * cal_hypn[len(cal_hypn)-1])
import sys
sys.stdin = open('염라대왕.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dic = {input().strip() for i in range(N)}
    dic = list(dic)
    dic.sort(reverse=True)
    print('#{}'.format(tc))
    a = 1
    while a <= 1\
            :
        for i in range(len(dic)-1, -1, -1):
            if dic[i] == '':
                del dic[i]
        for i in range(len(dic)-1, -1, -1):
            if len(dic[i]) == a:
                print(dic[i])
                del dic[i]
        a += 1
    [print(dic[i]) for i in range(len(dic))]


T = int(input())
for tc in range(T):
    N = int(input())
    print("#{}".format(tc+1))
    namebook = [[0] for _ in range(100)]
    for _ in range(N):
        temp = input().strip()
        namebook[len(temp)-1][0] += 1
        namebook[len(temp)-1].append(temp)
    for i in range(100):
        if namebook[i][0] > 0:
            temp_list = list(set(namebook[i][1:]))
            temp_list.sort()
            namebook[i][1:] = temp_list
            namebook[i][0] = len(temp_list)
    for i in range(100):
        for j in range(namebook[i][0]):
            print(namebook[i][j+1])
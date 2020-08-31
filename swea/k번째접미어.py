import sys
sys.stdin = open('kth.txt')




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    word = input()
    dic = []
    for i, a in enumerate(word):
        dic.append(word[i:])
    dic.sort()
    print('#{} {}'.format(tc, dic[N-1]))
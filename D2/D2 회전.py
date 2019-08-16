T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    words = list(map(int,input().split()))
    for i in range(M):
        words.append(words[0])
        del words[0]
    print('#{} {}'.format(test_case, words[0]))

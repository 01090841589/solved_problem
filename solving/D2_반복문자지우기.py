T = int(input())
for test_case in range(1, T+1):
    s = input()
    S = list(map(str,s))
    while True:
        buffer = len(S)
        for i in range(len(S)):
            if i == 0:
                comp = S[i]
            elif S[i] == comp:
                del S[i]
                del S[i-1]
                break
            else :
                comp = S[i]
        if len(S) == buffer:
            break
    print('#{} {}'.format(test_case, len(S)))
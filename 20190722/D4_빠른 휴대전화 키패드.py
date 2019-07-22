key_pad = [[], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
T = int(input())
for test_case in range(1, T+1):
    SN = input().split()
    S = int(SN[0])
    N = int(SN[1])
    s = []
    in_word = 0
    dic_word = 0
    for i in range(len(str(S))):
         s.append(key_pad[(S%10)-1])
         S //= 10
    s.reverse()
    word = input().split()
    for i in range(len(word)):
        if len(word[i]) == len(s):
            for j in range(len(s)):
                if word[i][j] in s[j]:
                    in_word += 1
                else:
                    break
            if in_word == len(s):
                dic_word += 1
                in_word = 0
    print('#{0} {1}'.format(test_case,dic_word))
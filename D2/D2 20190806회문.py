T = int(input())
for test_case in range(1, T+1):
    NM = list(map(int,input().split()))
    words = []
    for a in range(NM[0]):
        words.append(input())
    for i in range(NM[0]):
        word_row = ''
        for j in range(NM[0]):
            word_row += words[j][i]
        words.append(word_row)
    for word in words:
        for i in range(len(word)):
            for j in range(i, len(word)):
                if word[i] == word[j] and i != j:
                    comp_word = word[i:j+1]
                    if comp_word == comp_word[::-1]:
                        if len(comp_word) == NM[1]:
                            print('#{} {}'.format(test_case,comp_word))
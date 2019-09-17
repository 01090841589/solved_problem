import sys
sys.stdin = open('수진이.txt')
T = int(input())
for test_case in range(1,T+1):
    word = input()
    sortword = sorted(list(map(str, word)))
    print(sortword)
    word = ''.join(sortword)
    part_word = []
    total = 0
    for a in range(len(word)):
        for b in range(a+1, len(word)+1):
            part_word.append(word[a:b])
    for i in part_word:
        for j in range(len(i)//2):
            if i[j] == i[-1-j]:
                continue
            else:
                total -= 1
                break
        total += 1
    print('#{0} {1}'.format(test_case,total))
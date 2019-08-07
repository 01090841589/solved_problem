T= int(input())
for test_case in range(1, T+1):
    words = input()
    words = words.replace('a','')
    words = words.replace('e','')
    words = words.replace('i','')
    words = words.replace('o','')
    words = words.replace('u','')
    print('#{} {}'.format(test_case,words))
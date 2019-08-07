T = int(input())
for test_case in range(1, T+1):
    words = input()
    endoor = []
    for word in words:
        if word == '{' or word == '(':
            endoor += word
        elif word == '}':
            if len(endoor) == 0:
                endoor = ['1']
                break
            elif endoor[len(endoor)-1] == '{':
                endoor.pop()
            else:
                endoor = ['1']
                break
        elif word == ')':
            if len(endoor) == 0:
                endoor = ['1']
                break
            elif endoor[len(endoor)-1] == '(':
                endoor.pop()
            else:
                endoor = ['1']
                break
    if len(endoor) == 0:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))
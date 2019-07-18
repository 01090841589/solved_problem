T = int(input())
for test_case in range(1,T+1):
    line = []
    for inp in range(5):
        line.append((input()))
    len_line = []
    max_len = 0
    print('#{0} '.format(test_case),end='')
    for i in range(len(line)):
        len_line.append(len(line[i]))
        if len(line[i]) > max_len :
            max_len = len(line[i])
    for i in range(max_len):
        for j in range(len(line)):
            if len_line[j] > i:
                print(line[j][i],end='')
    print('')
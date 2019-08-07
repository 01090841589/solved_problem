
T = int(input())
for test_case in range(1, T+1):
    A = input().split()
    stack = []
    buf = 0
    for i in range(len(A)):
        try:
            A[i] = int(A[i])
        except:
            continue
    for i in A:
        if type(i) == int:
            stack.append(i)
        elif i == '+':
            if len(stack) < 2:
                print('#{} error'.format(test_case))
                break
            buf = stack.pop()
            buf += stack.pop()
            stack.append(buf)
        elif i == '-':
            if len(stack) < 2:
                print('#{} error'.format(test_case))
                break
            buf = stack.pop()
            buf -= stack.pop()
            stack.append(buf)
        elif i == '*':
            if len(stack) < 2:
                print('#{} error'.format(test_case))
                break
            buf = stack.pop()
            buf *= stack.pop()
            stack.append(buf)
        elif i == '/':
            if len(stack) < 2:
                print('#{} error'.format(test_case))
                break
            buf = stack.pop()
            buf = stack.pop() // buf
            stack.append(buf)
        elif i == '.':
            if len(stack) == 1:
                print('#{} {}'.format(test_case,stack[0]))
            else :
                print('#{} error'.format(test_case))


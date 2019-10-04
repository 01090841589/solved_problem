import sys
sys.stdin = open("스택수열.txt")


N = int(input())
arr = []
stack = []
k = 0
result = []
for i in range(N):
    arr.append(int(input()))
for i in range(1, N+1):
    if stack == []:
        stack.append(i)
        result.append('+')
    else:
        while stack != [] and stack[-1] == arr[k]:
            result.append('-')
            stack.pop()
            k += 1
        else:
            stack.append(i)
            result.append('+')
while stack != []:
    if stack[-1] == arr[k]:
        result.append('-')
        stack.pop()
        k += 1
    else:
        break

if stack == []:
    print('\n'.join(result))
else:
    print('NO')

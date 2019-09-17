import sys
sys.stdin = open("병합정렬.txt")

def divv(N):
    global result
    # if len(N) <=1:
    #     stack.append(N)
    #     return
    if len(N) == 3:
        stack.extend([N[:len(N)//2], N[len(N)//2:]])
        return
    if len(N) == 2:
        if N[0] > N[1]:
            result += 1
        stack.append([min(N[0], N[1]), max(N[0], N[1])])
        return
    divv(N[:len(N)//2])
    divv(N[len(N)//2:])



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = 0
    stack = []
    divv(lst)
    while len(stack) > 1:
        if len(stack[0]) > len(stack[1]):
            buf = []
            if stack[1][-1] > stack[2][-1]:
                result += 1
            while stack[1] and stack[2]:
                if stack[1][0] <= stack[2][0]:
                    buf.append(stack[1].pop(0))
                else:
                    buf.append(stack[2].pop(0))
            if stack[1]:
                for a in stack[1]:
                    buf.append(a)
            elif stack[2]:
                for a in stack[2]:
                    buf.append(a)
            stack.pop(2)
            stack[1] = buf
        else:
            buf = []
            if stack[0][-1] > stack[1][-1]:
                result += 1
            while stack[0] and stack[1]:
                if stack[0][0] <= stack[1][0]:
                    buf.append(stack[0].pop(0))
                else:
                    buf.append(stack[1].pop(0))
            if stack[0]:
                for a in stack[0]:
                    buf.append(a)
            elif stack[1]:
                for a in stack[1]:
                    buf.append(a)
            stack.pop(1)
            stack[0] = buf
    print('#{} {} {}'.format(tc, stack[0][N//2],result))
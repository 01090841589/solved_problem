from collections import deque

def solution(arrangement):
    answer = 0
    cnt = arrangement.count('(')
    depth = 0
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            depth += 1
        elif arrangement[i] == ')':
            if arrangement[i - 1] == '(':
                cnt -= 1
                depth -= 1
                answer += depth
            else:
                depth -= 1
    return answer+cnt


print(solution("()(((()())(())()))(())"))
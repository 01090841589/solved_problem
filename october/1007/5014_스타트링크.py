import sys
sys.stdin = open("스타트링크.txt")

from collections import deque

F, S, G, U, D = map(int, input().split())


stairs = [0] * (F+1)
result = 1000000
stack = deque()
stack.append(S)
stairs[S] = 1
while stack:
    idx = stack.popleft()
    if result <= stairs[idx]:
        continue
    if idx == G:
        if result > stairs[idx]:
            result = stairs[idx]
        continue
    if idx+U <= F and stairs[idx+U] == 0:
        stack.append(idx+U)
        stairs[idx+U] = stairs[idx]+1
    if idx-D > 0 and stairs[idx-D] == 0:
        stack.append(idx-D)
        stairs[idx-D] = stairs[idx]+1


if stairs[G]:
    print(result-1)
else:
    print('use the stairs')
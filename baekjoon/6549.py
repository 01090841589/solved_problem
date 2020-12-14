import sys
sys.stdin = open("6549.txt")

N = int(input())
inputs = list(map(int, input().split()))
res = 0
stack = []
for i, num in enumerate(inputs):
    if N == 0:
        N = num
        continue
    if not stack:
        stack.append([i, num])
        continue
    mini = 100010
    while stack:
        if stack[-1][1] <= num:
            if mini != 100010:
                stack.append([mini, num])
            else:
                stack.append([i, num])
            break
        else:
            if res < (i-stack[-1][0]) * stack[-1][1]:
                res = (i - stack[-1][0]) * stack[-1][1]
            mini = stack[-1][0]
            stack.pop()
            if not stack:
                stack.append([mini, num])
                break
for i, val in stack:
    if res < (N-i) * val:
        res = (N - i) * val
print(res)
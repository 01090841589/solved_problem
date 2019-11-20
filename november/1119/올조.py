import sys
sys.stdin = open("올조.txt")

from collections import deque
def find_low(N):
    if len(alpa) == 1:
        return True
    for i in range(N//2):
        if alpa[i] > alpa[(i*-1)-1]:
            return False
        elif alpa[i] < alpa[(i*-1)-1]:
            return True
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    alpa = deque()
    for i in range(N):
        alpa.append(input().strip())
    result = ''
    K = N
    for i in range(N):
        if find_low(K):
            result += alpa[0]
            alpa.popleft()
        else:
            result += alpa[-1]
            alpa.pop()
        K -= 1
    print("#{} ".format(tc), end='')
    for i in range(N):
        print(result[i], end='')
    print()
import sys
sys.stdin = open("숨바꼭질.txt")

from collections import deque
line = [100000] * 100002

N, K = map(int, input().split())
line[N] = 0
que = deque()
que.append([N, 0, [N]])
result = []
while que:
    num, scr, visited = que.popleft()
    if num > K:
        if line[K] > num - K:
            line[K] = scr+num-K
            result = visited + [-num]
            continue
    if scr == line[K]:
        result = visited
        break
    if scr > line[K]:
        continue
    if 0 < num*2 < 100001:
        if line[num*2] > scr+1:
            line[num*2] = scr+1
            que.append([num*2, scr+1, visited+[num*2]])

    if 0 <= num-1 < 100001:
        if line[num-1] > scr+1:
            line[num-1] = scr+1
            que.append([num-1, scr+1, visited+[num-1]])

    if 0 <= num+1 < 100001:
        if line[num+1] > scr+1:
            line[num+1] = scr+1
            que.append([num+1, scr+1, visited+[num+1]])

print(line[K])
for i in range(len(result)):
    if result[i] >= 0:
        print(result[i], end = " ")
    else:
        for k in range(-(result[i])-1, K-1, -1):
            print(k, end=' ')
print()




print(line[:100])
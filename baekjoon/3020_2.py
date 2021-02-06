import sys
sys.stdin = open("3020.txt")


N,H = map(int, sys.stdin.readline().split())

up = []
down = []
cnt = [0 for _ in range(H)]
for _ in range(N//2):
    down.append(int(sys.stdin.readline()))
    up.append(int(sys.stdin.readline()))

up.sort()
down.sort()
for i in range(H):
    l = 0
    r = N // 2
    m = -1
    while l < r:
        m = (r+l)//2
        if up[m] >= i+1:
            r = m
        elif up[m] < i+1:
            l = m+1
    cnt[i] = N//2-l
    if N//2-l == 0:
        for j in range(i,H):
            cnt[j] = 0
        break

for i in range(H):
    l = 0
    r = N // 2
    m = -1
    di = H-i
    while l < r:
        m = (r+l)//2
        if down[m] >= di:
            r = m

        elif down[m] < di:
            l = m+1
    cnt[i] += N//2-l
    if N//2-l == N//2:
        for j in range(i,H):
            cnt[j] = N//2
        break

ans = 0
min_cnt = min(cnt)
for i in range(H):
    if cnt[i] == min_cnt:
        ans += 1

print(min_cnt, ans)
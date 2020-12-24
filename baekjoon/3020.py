import sys
sys.stdin = open("3020.txt")

N, H = map(int, sys.stdin.readline().split())
up, down = [], []
for i in range(N):
    if i % 2:
        down.append(int(sys.stdin.readline()))
    else:
        up.append(int(sys.stdin.readline()))

res, res_cnt = N, 0
up.sort(reverse=True)
down.sort(reverse=True)
for h in range(H):
    up_d, down_d = (H - 1) - h, h
    left, right = 0, (N//2)-1
    ups = N//2

    while left <= right:
        mid = (left + right) // 2
        if up_d < up[mid]:
            left = mid + 1
        else:
            right = mid - 1
            if ups > mid:
                ups = mid

    left, right = 0, (N//2)-1
    downs = N//2
    while left <= right:
        mid = (left + right) // 2
        if down_d < down[mid]:
            left = mid + 1
        else:
            right = mid - 1
            if downs > mid:
                downs = mid
    if res > ups+downs:
        res = ups+downs
        res_cnt = 1
    elif res == ups+downs:
        res_cnt += 1

print(res, res_cnt)
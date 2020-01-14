import sys
sys.stdin = open("피자굽기.txt")

D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))
for i in range(D-1):
    if oven[i] < oven[i+1]:
        oven[i+1] = oven[i]
oven.insert(0, oven[0])
for i in range(N):
    if D <= 0:
        break
    left = 1
    right = D
    flag = 1
    while left <= right:
        mid = (left+right) // 2
        if pizza[i] <= oven[mid]:
            left = mid+1
            D = mid
            flag = 0
        else:
            right = mid-1
    if flag:
        D = 0
    D -= 1
if D > 0:
    print(D+1)
else:
    print(0)
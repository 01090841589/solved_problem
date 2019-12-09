import sys
sys.stdin = open("최대부분배열.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    result = -999999
    now = 0
    for i in range(N):
        arr.append(int(input()))
    for i in range(N):
        now += arr[i]
        if now < 0:
            now = 0
        if result < now:
            result = now
    print("#{} {}".format(tc, result))
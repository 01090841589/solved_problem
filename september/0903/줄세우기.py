import sys
sys.stdin = open('줄세우기.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(N):
        cnt = 1
        buf = arr[i]
        if result > N-i:
            continue
        for j in range(i+1, N):
            if arr[j] == buf+1:
                buf += 1
                cnt += 1
            if result-cnt > N-i:
                break
        if cnt > result:
            result = cnt
    print('#{} {}'.format(test_case, N-result))
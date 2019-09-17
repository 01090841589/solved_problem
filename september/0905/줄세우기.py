import sys
sys.stdin = open('줄세우기.txt')

def lis(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    print('#{} {}'.format(test_case,n-lis(list(map(int, input().split())))))
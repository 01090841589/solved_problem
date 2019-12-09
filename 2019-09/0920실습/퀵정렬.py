import sys
sys.stdin = open("퀵정렬.txt")

def quick_sort(x, left, right):
    if left < right:
        mid = divide(x, left, right)
        quick_sort(x, left, mid-1)
        quick_sort(x, mid+1, right)
        
def divide(x, l_idx, r_idx):
    buf = x[l_idx]
    buf_idx = l_idx
    while l_idx <= r_idx:
        while l_idx <= r_idx and x[l_idx] <= buf:
            l_idx += 1
        while l_idx <= r_idx and x[r_idx] >= buf:
            r_idx -= 1
        if l_idx <= r_idx:
            x[l_idx], x[r_idx] = x[r_idx], x[l_idx]
            l_idx += 1
            r_idx -= 1
    x[buf_idx], x[r_idx] = x[r_idx], x[buf_idx]
    return r_idx

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    print('#{} {}'.format(tc, arr[N//2]))
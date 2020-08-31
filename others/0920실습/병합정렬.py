import sys
sys.stdin = open("병합정렬.txt")

def merge_sort(lst):
    global cnt
    if len(lst) <= 1:
        return
    left = lst[:len(lst) // 2]
    merge_sort(left)
    right = lst[len(lst) // 2:]
    merge_sort(right)
    left_idx = 0
    right_idx = 0
    cng_idx = 0
    if left[-1] > right[-1]:
        cnt += 1
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            lst[cng_idx] = left[left_idx]
            left_idx += 1
            cng_idx += 1
        else:
            lst[cng_idx] = right[right_idx]
            right_idx += 1
            cng_idx += 1
    while left_idx < len(left):
        lst[cng_idx] = left[left_idx]
        left_idx += 1
        cng_idx += 1
    while right_idx < len(right):
        lst[cng_idx] = right[right_idx]
        right_idx += 1
        cng_idx += 1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    merge_sort(lst)
    print('#{} {} {}'.format(tc, lst[len(lst)//2], cnt))
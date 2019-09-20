import sys
sys.stdin = open("퀵정렬.txt")

def merge_sort(a):
    global cnt
    n = len(a)
    if n <= 1:
        return
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1 = 0
    i2 = 0
    ia = 0
    if g1[-1] > g2[-1]:
        cnt += 1
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    merge_sort(lst)
    print('#{} {} {}'.format(tc, lst[len(lst)//2], cnt))
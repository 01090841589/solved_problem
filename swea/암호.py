import sys
sys.stdin = open("암호.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    for a in range(K):
        i += M
        if i > len(arr):
            i = i%len(arr)
        if i == len(arr):
            arr.append(arr[-1]+arr[0])
        else:
            arr.insert(i, arr[i-1]+arr[i])
    print('#{}'.format(tc), end = ' ')
    try:
        for i in range(1, 11):
            print(arr[-i], end = ' ')
    except:
        print()
        continue
    print()


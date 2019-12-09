import sys
sys.stdin = open("이진탐색.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Nst = list(map(int, input().split()))
    Nst.sort()
    Mst = list(map(int, input().split()))
    cnt = 0
    for MM in Mst:
        l = 0
        r = N-1
        m = (l+r)//2
        left, right = 0, 0
        while True:
            if Nst[m] > MM:
                if left == 0:
                    left += 1
                    right = 0
                else:
                    break
                r = m-1
                m = (l+r)//2
            elif Nst[m] < MM:
                if right == 0:
                    right += 1
                    left = 0
                else:
                    break
                l = m+1
                m = (l+r)//2
            else:
                cnt += 1
                break
    print('#{} {}'.format(tc, cnt))
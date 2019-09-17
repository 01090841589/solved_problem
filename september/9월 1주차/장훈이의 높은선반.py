import sys
sys.stdin = open('장훈이.txt')


def top(K, score):
    global result
    if score >= B:
        if result > score-B:
            result = score-B
    if K >= N:
        return
    top(K+1, score+men[K])
    top(K+1, score)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    men = list(map(int, input().split()))
    result = 999999
    men.sort(reverse=True)
    top(0, 0)
    print('#{} {}'.format(tc, result))
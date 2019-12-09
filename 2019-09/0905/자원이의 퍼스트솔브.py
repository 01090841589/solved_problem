import sys
sys.stdin = open('퍼스트솔브.txt')

def solve(k, scr, tim):
    global result
    if k == N:
        if result < scr:
            result = scr
        return
    if tim >= SF[k][0]:
        return
    if (N-k)+scr <= result:
        return
    if tim+SF[k][1] <= SF[k][0]:
        solve(k+1, scr+1, tim+SF[k][1])
    solve(k+1, scr, tim)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    SF = []
    for i in range(N):
        S = list(map(int, input().strip().split()))
        SF.append([S[1], S[0]])
    SF.sort()
    solve(0, 0, 0)
    print(SF)
    print('#{} {}'.format(tc, result))
import sys
sys.stdin = open('퇴사.txt')

def score(k, scr):
    global result
    if k > N:
        return
    if k == N:
        if result < scr:
            result = scr
        return
    score(k+price[k][0], scr+price[k][1])
    score(k+1, scr)

N = int(input())
price = [list(map(int, input().split())) for _ in range(N)]
result = 0
score(0, 0)
print(result)

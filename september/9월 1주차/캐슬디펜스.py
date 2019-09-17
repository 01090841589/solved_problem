import sys
sys.stdin = open('castle.txt')

def attack(K, D):
    global score
    for dis in range(1, D+1):
        for x in range(-dis+1, dis):
            y = dis-abs(x)-1
            if 0<= (N-1-y) < N and 0 <= (x+K) < M and MAPS[N-1-y][x+K]:
                stack.append([(N - 1) - y,x + K])
                return

N, M, D = map(int, input().split())
MAP = [list(map(int, input().split())) for i in range(N)]
total = 0
for a in range(M-2):
    for b in range(a+1, M-1):
        for c in range(b+1, M):
            MAPS = [MAP[i][:] for i in range(N)]
            score = 0
            for cas in range(N):
                stack = []
                attack(a, D)
                attack(b, D)
                attack(c, D)
                while stack:
                    [y, x] = stack.pop()
                    if MAPS[y][x]:
                        MAPS[y][x] = 0
                        score += 1
                del MAPS[N-1]
                MAPS.insert(0, [0]*M)
            if total < score:
                total = score

print(total)
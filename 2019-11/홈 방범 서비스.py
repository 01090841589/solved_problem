import sys
sys.stdin = open("홈 방범 서비스.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    home = []
    res = 1
    for y in range(N):
        for x in range(N):
            if MAP[y][x] == 1:
                home.append([y, x])     # 집 위치 검색
    for y in range(N):
        for x in range(N):
            dis = []
            for a in range(len(home)):
                dis.append(abs(y-home[a][0])+abs(x-home[a][1]))
            if res >= len(dis):
               break
            dis.sort(reverse=True)
            for i in dis:
                if (i+1)*(i+1)+i*i <= (len(dis)-dis.index(i))*M:
                    res = max(res, len(dis)-dis.index(i))
    print('#{} {}'.format(tc, res))

M,N = map(int, input().split())

factory = [list(map(int, input().split())) for _ in range(M)]

from collections import deque

#동남서북으로 함
dx = [1,0,-1,0]
dy = [0,1,0,-1]

sy,sx, sk = map(int, input().split())
ey,ex, ek = map(int, input().split())

# 문제에서는 1234 순으로 동서남북이라 2나 3이 들어왔을때 바꿔줌
if sk == 3:
    sk = 2
elif sk == 2:
    sk == 3
if ek == 3:
    ek = 2
elif ek == 2:
    ek = 3

visited = [[[99999,99999,99999,99999] for _ in range(N)] for _ in range(M)]
def bfs():
    q = deque()
    # 시작지점,방향 비지티드 체크
    visited[sy-1][sx-1][sk-1] = 0
    q.append([sx-1,sy-1,sk-1])

    while q:
        tx,ty,tk = q.popleft()
        for k in range(4):
            #현재 방향일 경우
            if k == tk:
                for i in range(1,4):
                    # 1칸씩 보면서 진행함
                    nx,ny = tx+dx[k]*i,ty+dy[k]*i
                    if 0<=nx<N and 0<= ny <M:
                        # 벽이 아니면
                        if factory[ny][nx] == 0:
                            # 행동수 비지티드에 +1
                            if visited[ny][nx][tk] > visited[ty][tx][tk]+1:
                                visited[ny][nx][tk] = visited[ty][tx][tk] +1
                                q.append([nx,ny,tk])
                        # 벽 만나면 브레이크
                        else: break
            #다른 방향일 경우
            else:
                # 방향이 90도 차이 나는 경우
                if k == (tk+1)%4 or k == (tk+3)%4:
                    cn = 1
                # 180도 차이 나는 경우
                elif k == (tk+2)%4:
                    cn = 2
                # cn(행동수추가)
                if visited[ty][tx][k] > visited[ty][tx][tk]+ cn:
                    visited[ty][tx][k] = visited[ty][tx][tk]+ cn
                    q.append([tx,ty,k])
    return visited[ey-1][ex-1][ek-1]
print(bfs())
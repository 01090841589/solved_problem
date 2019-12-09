import sys
sys.stdin = open("색종이만들기.txt")

def colorpaper(nx, mx, ny, my):
    global blue, white
    flag = MAP[ny][nx]
    kx = (mx-nx)//2
    ky = (my-ny)//2
    if kx == 0:
        if flag:
            blue += 1
        else:
            white += 1
        return
    for i in range(ny, my):
        for j in range(nx, mx):
            if MAP[i][j] != flag:
                colorpaper(nx, mx-kx, ny, my-ky)
                colorpaper(nx+kx, mx, ny, my-ky)
                colorpaper(nx, mx-kx, ny+ky, my)
                colorpaper(nx+kx, mx, ny+ky, my)
                return
    if flag:
        blue += 1
    else:
        white += 1

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
blue, white = 0, 0

colorpaper(0, N, 0, N)
print(white)
print(blue)
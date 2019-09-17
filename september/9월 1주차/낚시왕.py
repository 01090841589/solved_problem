import sys
sys.stdin = open('fishing.txt')

def move(fishes):
    MAP = [[[0, 0, 0]] * C for _ in range(R)]
    for i in range(len(fishes)):
        print(i, DIR[fishes[i][3]-1][0], DIR[fishes[i][3]-1][1])
        fishes[i] = [fishes[i][0]+(DIR[fishes[i][3]-1][0])*fishes[i][2], fishes[i][1]+(DIR[fishes[i][3]-1][1])*fishes[i][2], fishes[i][2], fishes[i][3], fishes[i][4]]
        while fishes[i][0] > R or fishes[i][0] <= 0:
            if abs(fishes[i][0]) > R*2:
                if fishes[i][0] > 0:
                    fishes[i][0] %= (R * 2)
                else:
                    fishes[i][0] = ((fishes[i][0] * -1) % R * 2 )* (-1)
            if fishes[i][0] > R:
                fishes[i][0] -= R
            if fishes[i][0] <= 0:
                fishes[i][0] = fishes[i][0]*(-1)+2
        while fishes[i][1] > C or fishes[i][1] <= 0:
            if fishes[i][1] > C:
                fishes[i][1] -= C
            if fishes[i][1] <= 0:
                fishes[i][1] = fishes[i][1]*(-1)+2
    print(fishes)


DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]
# s, d, z
R, C, M = map(int, input().split())
MAP = [[[0, 0, 0]] * C for _ in range(R)]
fishes = [list(map(int, input().split())) for _ in range(M)]
fisher = 0
print(fishes)
[print(MAP[i]) for i in range(R)]
for shark in fishes:
    MAP[shark[0]-1][shark[1]-1] = [shark[2], shark[3], shark[4]]
print()
[print(MAP[i]) for i in range(R)]
score = 0
#for
for catch in range(R):
    if MAP[catch][fisher][0] != 0:
        for i in range(M-1, -1, -1):
            if fishes[i][0] == catch+1 and fishes[i][1] == fisher+1:
                del fishes[i]
        MAP[catch][fisher] = [0, 0, 0]
        score += 1
print(fishes)
move(fishes)

[print(MAP[i]) for i in range(R)]
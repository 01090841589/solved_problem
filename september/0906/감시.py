import sys
sys.stdin = open('감시.txt')
cam = [
[],
[[[0, 1]], [[1, 0]], [[0, -1]], [[-1, 0]]],
[[[0, 1], [0, -1]], [[1, 0], [-1, 0]]],
[[[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]], [[-1, 0], [0, 1]]],
[[[0, 1], [1, 0], [0, -1]], [[1, 0], [0, -1], [-1, 0]], [[0, -1], [-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]]],
[[[0, 1], [1, 0], [0, -1], [-1, 0]]]
]

def watch(k):
    global result
    if k == len(camera):
        # light_go()
        for i in range(len(light)):
            [y, x, C] = camera[i]
            arr = cam[C][light[i]]
            for go in arr:
                i = 1
                while True:
                    Y = y+go[0]*i
                    X = x+go[1]*i
                    if MAP[Y][X] == 0:
                        MAP[Y][X] = 9
                    elif MAP[Y][X] == 6:
                        break
                    i += 1
        cnt = 0
        for yy in range(1, N+1):
            for xx in range(1, M+1):
                if MAP[yy][xx] == 0:
                    cnt += 1
        if result > cnt:
            result = cnt

        for i in range(len(light)):
            [y, x, C] = camera[i]
            arr = cam[C][light[i]]
            for go in arr:
                i = 1
                while True:
                    Y = y+go[0]*i
                    X = x+go[1]*i
                    if MAP[Y][X] == 9:
                        MAP[Y][X] = 0
                    elif MAP[Y][X] == 6:
                        break
                    i += 1
        return
    [y, x, c] = camera[k]
    for arrs in range(len(cam[c])):
        light.append(arrs)
        watch(k+1)
        light.pop()

# def light_go():

N, M = map(int, (input().split()))
MAP = [[6]+list(map(int, input().split()))+[6] for _ in range(N)]
MAP.insert(0, [6]*(M+2))
MAP.append([6]*(M+2))
camera = []
result = 999999999
for y in range(1, N+1):
    for x in range(1, M+1):
        if 0 < MAP[y][x] < 6:
            camera.append([y, x, MAP[y][x]])
light = []
watch(0)
print(result)

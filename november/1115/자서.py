import sys
sys.stdin = open("자석.txt")


T = int(input())
for tc in range(1, T+1):
    k = int(input())
    MAP = [list(map(int, input().split())) for _ in range(4)]
    comm = [list(map(int, input().split())) for _ in range(k)]
    for c in comm:
        if c[1] == 1:
            MAP[c[0]-1].insert(0, MAP[c[0]-1].pop())
        else:
            MAP[c[0]-1].append(MAP[c[0]-1].pop(0))
        buf = c[1]
        for i in range(c[0]-2, -1, -1):
            if buf == 1:
                if MAP[i][2] != MAP[i+1][7]:
                    MAP[i].append(MAP[i].pop(0))
                    buf = -1
                else:
                    break
            else:
                if MAP[i][2] != MAP[i+1][5]:
                    MAP[i].insert(0, MAP[i].pop())
                    buf = 1
                else:
                    break
        buf = c[1]
        for i in range(c[0], 4):
            if buf == 1:
                if MAP[i][6] != MAP[i-1][3]:
                    MAP[i].append(MAP[i].pop(0))
                    buf = -1
                else:
                    break
            else:
                if MAP[i][6] != MAP[i-1][1]:
                    MAP[i].insert(0, MAP[i].pop())
                    buf = 1
                else:
                    break

    print('#{} {}'.format(tc, MAP[0][0]+MAP[1][0]*2+MAP[2][0]*4+MAP[3][0]*8))



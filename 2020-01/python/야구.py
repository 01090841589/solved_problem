import sys
sys.stdin = open("야구.txt")

from itertools import permutations
inning = int(input())
batters =[ list(map(int, input().split())) for _ in range(inning)]
res = 0
for play in permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):
    play = list(play)
    play.insert(3, 0)
    scr = 0
    now = 0
    for innings in range(inning):
        out = 0
        bases = 0
        while out < 3:
            # 비트마스킹
            if batters[innings][play[now]] == 0:
                out += 1
            elif batters[innings][play[now]] == 1:
                if bases & 4:
                    scr += 1
                    bases -= 4
                if bases & 2:
                    bases += 2
                if bases & 1:
                    bases += 1
                bases += 1
            elif batters[innings][play[now]] == 2:
                if bases & 4:
                    scr += 1
                    bases -= 4
                if bases & 2:
                    scr += 1
                    bases -= 2
                if bases & 1:
                    bases += 3
                bases += 2
            elif batters[innings][play[now]] == 3:
                if bases & 4:
                    scr += 1
                    bases -= 4
                if bases & 2:
                    scr += 1
                    bases -= 2
                if bases & 1:
                    scr += 1
                    bases -= 1
                bases += 4
            elif batters[innings][play[now]] == 4:
                if bases & 4:
                    scr += 1
                    bases -= 4
                if bases & 2:
                    scr += 1
                    bases -= 2
                if bases & 1:
                    scr += 1
                    bases -= 1
                scr += 1
            now = (now+1)%9
    if res < scr:
        res = scr
print(res)



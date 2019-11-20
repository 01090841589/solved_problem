import sys
sys.stdin = open("inter.txt")

from math import isclose, inf

T = int(input())
for tc in range(1, T+1):
    rac = list(map(int, input().split()))
    line = list(map(int, input().split()))
    print(rac, line)

    if line[1]-line[3] == 0 or line[0]-line[2] == 0:

        print(4)
    else:
        ron = (line[1]-line[3])/(line[0]-line[2])
        print(ron)

        lx, ly, rx, ry = line
        print(lx)
        a = ly-(lx*ron)
        print(a)
        b = ly+(lx*ron)
        print(b)
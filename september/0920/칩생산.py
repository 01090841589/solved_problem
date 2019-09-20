import sys
sys.stdin = open("칩생산.txt")

def selection(chip, cnt):
    global result
    chips = chip[:]
    if chips:
        k = chips.pop(0)
        if k % W != 0 and (k +(W-1)) in chips:
            chips.remove(k+(W-1))
        if (k + 1) in chips:
            chips.remove(k+1)
        if (k + W) in chips:
            chips.remove(k + W)
        if (k + W + 1) in chips:
            chips.remove(k + W + 1)
        selection(chips[:], cnt+1)
        selection(chip)
    # else:
    #     if result < cnt:
    #         result = cnt


T = int(input())
for tc in range(1, 3):
    H, W = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]
    [print(MAP[i]) for i in range(H)]
    print()
    result = 0
    chip = []
    # print(len(chip), chip)
    k = 0
    N = H*W
    while True:
        if k == N:
            [print(MAP[i]) for i in range(H)]
            print()
            break
        y = k // W
        x = k % W
        if x < W-1 and y < H-1:
            if MAP[y][x] == 0 and MAP[y][x+1] == 0 and MAP[y+1][x] == 0 and MAP[y+1][x+1] == 0:
            #     MAP[y][x], MAP[y][x+1], MAP[y+1][x], MAP[y+1][x+1] = 2, 2, 2, 2
                chip.append(k)
        k += 1
    for i in range(len(chip)):
        selection(chip[i:], 0)
        # if k == N:
        #     if chip:
        #         if chip[0] > W:
        #             break
        #         a = chip.pop()
        #         y = a // W
        #         x = a % W
        #         MAP[y][x], MAP[y][x + 1], MAP[y + 1][x], MAP[y + 1][x + 1] = 0, 0, 0, 0
        #         k = a+1
    print(result)
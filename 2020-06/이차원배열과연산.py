import sys
sys.stdin = open("이차원배열과연산.txt")

r, c, k = map(int, input().split())
MAP = [list(map(int, (input().split()))) for _ in range(3)]
xlen, ylen = 3, 3
scr = 0
while scr < 101:
    # print(scr)
    if r <= ylen and c <= xlen:
        if MAP[r-1][c-1] == k:
            break
    if xlen <= ylen: #R연산
        res = []
        max_len = 0
        for i in range(ylen):
            nums = dict()
            for j in range(xlen):
                if MAP[i][j] == 0:
                    continue
                if nums.get(MAP[i][j]) == None:
                    nums[MAP[i][j]] = 1
                else:
                    nums[MAP[i][j]] += 1
            array = []
            for key, value in nums.items():
                array.append([key, value])
            array.sort()
            array.sort(key=lambda k:k[1])
            if max_len < len(array)*2:
                max_len = len(array)*2
            buf = []
            for ar in range(len(array)):
                buf.append(array[ar][0])
                buf.append(array[ar][1])
            res.append(buf)
        for i in range(ylen):
            res[i] = res[i] + [0] * (max_len-len(res[i]))
        print(scr+1)
        [print(res[i]) for i in range(ylen)]
        print()
        MAP = res
    else: #C연상
        rev_MAP = [[0] * ylen for _ in range(xlen)]
        for y in range(ylen):
            for x in range(xlen):
                rev_MAP[x][y] = MAP[y][x]

        res = []
        xlen, ylen = ylen, xlen
        max_len = 0
        for i in range(ylen):
            nums = dict()
            for j in range(xlen):
                if rev_MAP[i][j] == 0:
                    continue
                if nums.get(rev_MAP[i][j]) == None:
                    nums[rev_MAP[i][j]] = 1
                else:
                    nums[rev_MAP[i][j]] += 1
            array = []
            for key, value in nums.items():
                array.append([key, value])
            array.sort()
            array.sort(key=lambda k: k[1])
            if max_len < len(array) * 2:
                max_len = len(array) * 2
            buf = []
            for ar in range(len(array)):
                buf.append(array[ar][0])
                buf.append(array[ar][1])
            res.append(buf)
        for i in range(ylen):
            res[i] = res[i] + [0] * (max_len - len(res[i]))
        # [print(res[i]) for i in range(ylen)]
        rev_res = [[0] * ylen for _ in range(max_len)]
        for y in range(ylen):
            for x in range(max_len):
                rev_res[x][y] = res[y][x]
        print(scr+1)
        [print(rev_res[i]) for i in range(max_len)]
        print()
        MAP = rev_res

    xlen = len(MAP[0])
    ylen = len(MAP)
    scr += 1
if scr == 101:
    print(-1)
else:
    print(scr)



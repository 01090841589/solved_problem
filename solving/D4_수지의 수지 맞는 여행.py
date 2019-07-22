DIR = ((1, 0), (-1, 0), (0, -1), (0, 1))
R = 3
C = 6
def check(y, x, i):
    global R, C
    cnt = 0
    while True:
        y = y + DIR[i][0]
        x = x + DIR[i][1]
        if y >= 0 and y < R and x >= 0 and x < C:
            if island[y][x] != '0':
                cnt += 1
            elif island[y][x] == '0':
                break
        else:
            break
def remove_island(spell,island):
    for lend in range(len(island)):
        island[lend] = island[lend].replace(spell,'0')

x, y = 0, 0
island = ['HFDFFB', 'AJHGDH', 'DGAGEH']
for i in range(len(island)):
    print(island[i])
remove_island(island[y][x],island)
for k in range(4):
    check(x, y, k)
for i in range(len(island)):
    print(island[i])
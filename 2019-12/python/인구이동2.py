NM = input().split(' ')
N = int(NM[0])
M = int(NM[1])
W = []
B = []
R = []
line = []
total = []
cal = N * M
for i in range(N):
    text = input()
    line.append(text)
    total.append(0)
total[0] = len(line[0]) - line[0].count('W')
total[len(line) - 1] = len(line[len(line) - 1]) - line[len(line) - 1].count('R')
for White in range(len(line) - 3, -1, -1):  # 3 2 1 0
    for count_White in range(1, White + 1):  # 123 12 1 -
        total[count_White] = len(line[count_White]) - line[count_White].count('W')
    for count_Blue in range(len(line) - 2, White, -1):  # 0 01 012 0123
        # len(line)-White 로 역순
        total[count_Blue] = len(line[count_Blue]) - line[count_Blue].count('B')
    if sum(total) < cal:
        cal = sum(total)
    for count_Red in range(len(line) - 2, White + 1, -1):  # 0 01 012 0123
        total[count_Red] = len(line[count_Red]) - line[count_Red].count('R')
        if sum(total) < cal:
            cal = sum(total)
print(cal)
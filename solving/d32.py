N = 5
isle = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 2],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 2, 0, 0]
]
isle3 = [
[3, 0, 0, 0, 0, 0, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
]
isle1 = [
[0, 1, 1, 0, 0],
[0, 0, 1, 0, 3],
[0, 1, 0, 1, 0],
[0, 0, 0, 0, 0],
[1, 0, 5, 0, 0]
]
stair = []
length = []
go_stair1 = []
go_stair2 = []
go_stair = []
stair_wait1 = []
stair_wait2 = []
for i in range(len(isle)):
    for j in range(len(isle)):
        if isle[i][j] > 1:
            stair.append([i,j,isle[i][j]])
# for i in range(len(isle)):
#     print(isle[i])
print(stair)
# stair[0][0] stair[0][1]
# stair[1][0] stair[1][1]

for i in range(len(isle)):
    for j in range(len(isle)):
        if isle[i][j] == 1:
            length.append([i, j, abs(i-stair[0][0])+abs(j-stair[0][1]), abs(i-stair[1][0])+abs(j-stair[1][1])])
print(length)
for cal_len in length:
    go_stair1.append([cal_len[2],1])
    go_stair2.append([cal_len[3],2])

print(go_stair1)
print(go_stair2)

for i in range(len(go_stair1)):
    if abs(go_stair1[i][0]-go_stair2[i][0]) > max(stair[0][2], stair[1][2]):
        if length[i][2] < length[i][3]:
            go_stair.append([i, length[i][0], length[i][1], length[i][2], 1])
        elif length[i][2] > length[i][3]:
            go_stair.append([i, length[i][0], length[i][1], length[i][3], 2])
go_stair.sort(reverse=True)
for i in go_stair:
    if i[4] == 1:
        stair_wait1.append(stair[0][2]+length[i[0]][2])
        del length[i[0]]
        del go_stair1[i[0]]
        del go_stair2[i[0]]
    else :
        stair_wait2.append(stair[0][2]+length[i[0]][3])
        del length[i[0]]
        del go_stair1[i[0]]
        del go_stair2[i[0]]
print(stair_wait1,stair_wait2)
print(length, go_stair1, go_stair2)
min = len(isle)
min_length = len(isle)*2
for i in range(len(length)):
    if abs(length[i][3]-length[i][2]) < min :
        min = abs(length[i][3]-length[i][2])
for i in range(len(length)):
    if abs(length[i][3]-length[i][2]) == min :
        if length[i][3]+length[i][2] < min_length :
            min_length = length[i][3]+length[i][2]
print(min,min_length)
for i in range(len(length)-1,-1,-1):
    if length[i][3]+length[i][2] == min_length :
        print(length[i])
        if length[i][2]+ stair[0][2] > length[i][3]+ stair[0][2] and len(stair_wait1) < 3:
            stair_wait1.append(stair[0][2] + length[i][2])
            del length[i]
            del go_stair1[i]
            del go_stair2[i]
        elif len(stair_wait2) < 3:
            stair_wait2.append(stair[0][2] + length[i][2])
            del length[i]
            del go_stair1[i]
            del go_stair2[i]
print(stair_wait1, stair_wait2)
    # if i[4] == 1:
    #     stair_wait1.append(stair[0][2]+length[i[0]][2])
    #     del length[i[0]]
    #     del go_stair1[i[0]]
    #     del go_stair2[i[0]]
    # else :
    #     stair_wait2.append(stair[0][2]+length[i[0]][3])
    #     del length[i[0]]
    #     del go_stair1[i[0]]
    #     del go_stair2[i[0]]




# 10
# 5
# 0 1 1 0 0
# 0 0 1 0 3
# 0 1 0 1 0
# 0 0 0 0 0
# 1 0 5 0 0
# 5
# 0 0 1 1 0
# 0 0 1 0 2
# 0 0 0 1 0
# 0 1 0 0 0
# 1 0 5 0 0
# 6
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 1 0 0 0 0
# 2 0 1 0 0 0
# 0 0 2 0 0 0
# 6
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 1 0 0 0 0 0
# 0 0 0 2 0 4
# 7
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 4
# 0 0 0 0 1 0 0
# 1 0 0 1 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 2 0 0 0 0 0
# 7
# 0 0 0 0 0 0 0
# 7 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0
# 2 0 0 0 0 1 0
# 0 0 0 0 0 0 0
# 8
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 2 0 0 0 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 0 0 1 0 0 0
# 8
# 3 0 0 0 0 0 5 0
# 0 0 0 0 0 0 0 0
# 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 1 0 1 1 0 0 0 0
# 0 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 9
# 0 0 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 8
# 7 0 0 0 0 1 0 0 0
# 0 0 0 0 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 1 0 0 0 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 10
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 1 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 3 0 1 0 1 0 0 0 0 2
# 1 1 0 0 1 0 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
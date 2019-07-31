T = 1
K = 2
mag_1 = [0, 0, 1, 0, 0, 1, 0, 0]

mag_2 = [1, 0, 0, 1, 1, 1, 0, 1]

mag_3 = [0, 0, 1, 0, 1, 1, 0, 0]

mag_4 = [0, 0, 1, 0, 1, 1, 0, 1]

move = [[1,1], [3,-1]]

for num in move:
    if num[0] == 1:
        if num[1] == 1:
            a = mag_1.pop()
            mag_1.insert(0,a)
        else :
            a = mag_1[0]
            del mag_1[0]
            mag_1.append(a)
print(mag_1)
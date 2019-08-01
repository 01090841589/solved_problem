T = 1
K = 2
mag_1 = [0, 0, 1, 0, 0, 1, 0, 0]
mag_2 = [1, 0, 0, 1, 1, 1, 0, 1]
mag_3 = [0, 0, 1, 0, 1, 1, 0, 0]
mag_4 = [0, 0, 1, 0, 1, 1, 0, 1]
move = [[1,1], [3,-1]]
magni = [[0, 0, 1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 0, 1]]
def move_mag(mag,a, c,gone):
    if c == 1:
        A = mag.pop()
        mag.insert(0, A)
        if 0<= a+1 <4 and a+1 not in gone:
            gone.append(a+1)
            print(gone,c)
            if mag[3] != magni[a+1][6]:
                move_mag(magni[a+1], a+1,-c,gone)
        if 0<= a-1 <4 and a-1 not in gone:
            gone.append(a-1)
            print(gone,c)
            if mag[7] != magni[a-1][2]:
                move_mag(magni[a-1], a-1,-c,gone)
    else:
        A = mag[0]
        del mag[0]
        mag.append(A)
        if 0<= a-1 <4 and a-1 not in gone:
            gone.append(a-1)
            print(gone,c)
            if mag[5] != magni[a-1][2]:
                move_mag(magni[a-1], a-1,-c,gone)
        if 0<= a+1 <4 and a+1 not in gone:
            gone.append(a+1)
            print(gone,c)
            if mag[1] != magni[a+1][6]:
                move_mag(magni[a+1], a+1,-c,gone)
    return mag
def cascade(x):
    if 0 < x < 5:
        mag_2 = move_mag(mag_2,-num[1])

for num in move:
    gone = []
    a = num[0]-1
    gone.append(a)
    magni[num[0]-1] = move_mag(magni[num[0]-1],a,num[1],gone)
    print(magni[0])
    print(magni[1])
    print(magni[2])
    print(magni[3])
    print()
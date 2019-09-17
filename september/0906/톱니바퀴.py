import sys
sys.stdin = open('청소기.txt')

magni = [list(map(int, input())) for _ in range(4)]
K = int(input())
move = [list(map(int, input().split())) for _ in range(K)]
def move_mag(mag,a, c,gone):
    if c == 1:
        A = mag.pop()
        mag.insert(0, A)
        if 0<= a+1 <4 and a+1 not in gone:
            gone.append(a+1)
            if mag[3] != magni[a+1][6]:
                move_mag(magni[a+1], a+1,-c,gone)
        if 0<= a-1 <4 and a-1 not in gone:
            gone.append(a-1)
            if mag[7] != magni[a-1][2]:
                move_mag(magni[a-1], a-1,-c,gone)
    else:
        A = mag[0]
        del mag[0]
        mag.append(A)
        if 0<= a-1 <4 and a-1 not in gone:
            gone.append(a-1)
            if mag[5] != magni[a-1][2]:
                move_mag(magni[a-1], a-1,-c,gone)
        if 0<= a+1 <4 and a+1 not in gone:
            gone.append(a+1)
            if mag[1] != magni[a+1][6]:
                move_mag(magni[a+1], a+1,-c,gone)
    return mag
for num in move:
    gone = []
    a = num[0]-1
    gone.append(a)
    magni[num[0]-1] = move_mag(magni[num[0]-1],a,num[1],gone)
total = magni[0][0]+magni[1][0]*2+magni[2][0]*4+magni[3][0]*8
print(total)
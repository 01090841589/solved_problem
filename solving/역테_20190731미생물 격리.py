T = 1
DIR = [[-1, 0],[1, 0],[0, -1], [0,1]]
NMK = list(map(int,input().split()))
cell = []
for i in range(NMK[2]):
    one_cell = list(map(int,input().split()))
    cell.append(one_cell)
print(cell)
mat = []
def cell_go(cel):
    print('이전꺼',cel,end=' ')
    Y = cel[0]+DIR[cel[3]-1][0]
    X = cel[1]+DIR[cel[3]-1][1]
    if X == 0 or Y == 0 or X == (NMK[0]-1) or Y == (NMK[0]-1) :
        cel[2] = int(cel[2]/2)
        if cel[3] % 2:
            cel[3] += 1
        else:
            cel[3] -= 1
    print('바뀐거', [Y, X, cel[2], cel[3]])
    return [Y, X, cel[2], cel[3]]
#  --------------------------------------------------
for tc in range(NMK[1]):
    for i in range(NMK[0]):
        mat.append([0]*NMK[0])
    for i in cell:
        mat[i[0]][i[1]]=i[2]
    # ----------------------------------------------------
    for i in range(1):
        for i, cells in enumerate(cell):
            cell[i] = cell_go(cells)
        print('------------------------------------')
    cell_sum = []
    for i in cell:
        if len(cell_sum) == 0:
            cell_sum.append(i)
        else:
            for lo in range(len(cell_sum)):
                if i[0] == cell_sum[lo][0] and i[1] == cell_sum[lo][1]:
                    cell_sum[lo].extend([i[2],i[3]])
                    break
                elif lo == len(cell_sum)-1:
                    cell_sum.append(i)
    print(cell_sum)
    for i, ce in enumerate(cell_sum):
        if len(ce) > 4:
            comp_cell = ce[2]
            max_cell = ce[2]
            loc_cell = ce[3]
            print(ce,comp_cell)
            for num in range(4, len(ce), 2):
                if ce[num] > max_cell:
                    loc_cell = ce[num+1]
                    max_cell = ce[num]
                    print(comp_cell,ce[num])
                comp_cell += ce[num]
            cell_sum[i] = [ce[0],ce[1],comp_cell,loc_cell]
    print(cell_sum)
    cell = cell_sum
    # for i in range(NMK[0]):
    #     print(mat[i])
    total = 0
for i in cell:
    total += i[2]
print(total)
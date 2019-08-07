T = 1
chance = 1
NK = [5, 1]
DIR = [[-1,0], [0,1], [1,0], [0,-1]]
mat = [
[9, 3, 2, 3, 2],
[6, 3, 1, 7, 5],
[3, 4, 8, 9, 9],
[2, 3, 7, 7, 7],
[7, 6, 5, 5, 8],
]
def find_route(XY,route_cnt):
    comp = mat[XY[0]][XY[1]]
    route.append(XY)
    cnt = 0

    for i in range(4):
        Y = XY[0] + DIR[i][0]
        X = XY[1] + DIR[i][1]
        print(XY, Y, X,end=' ')
        if 0 <= Y < NK[0] and 0 <= X < NK[0]:
            if mat[Y][X] < comp:
                print('통과',end=' ')
                print()
                find_route([Y,X],route_cnt+1)
            else :
                cnt += 1
        else :
            cnt += 1
        if cnt == 4:
            print('여기가 막다른길 위치{},{}, 이동거리{}'.format(Y,X,route_cnt))
        print()
stack = []
max = 0
start = []
for i in range(NK[0]):
    for j in range(NK[0]):
        if mat[i][j] > max:
            max = mat[i][j]
print(max)
for i in range(NK[0]):
    for j in range(NK[0]):
        if mat[i][j] == max:
            start.append([i, j])
print(start)
for go in start:
    route = []
    route_cnt = 0
    find_route(go,route_cnt)
    print()
print(route)
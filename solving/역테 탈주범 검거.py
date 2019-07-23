tunnal = [[[-1, 0], [1, 0], [0,-1], [0, 1]], [[-1, 0], [1, 0]], [[0, -1], [0, 1]], [[-1, 0], [0, 1]], [[1, 0], [0, 1]], [[1, 0], [0, -1]], [[-1, 0], [0, -1]]]
T = int(input())
for test_case in range(1,T+1):
    NMRCL = list(map(int,input().split()))
    N = NMRCL[0]
    M = NMRCL[1]
    R = NMRCL[2]
    C = NMRCL[3]
    L = NMRCL[4]
    tunnal_map = []
    x_map = [0 for a in range(M)]
    tunnal_map = [x_map[:] for a in range(N)]
    pipe = []
    for pip in range(N):
        pipe.append(list(map(int,input().split())))
    # for a in range(N):
    #     print(tunnal_map[a],pipe[a])
    # print()
    move = [R, C]
    running = []
    tunnal_map[move[0]][move[1]] = 1
    # for a in range(N):
    #     print(tunnal_map[a],pipe[a])
    # print()

    for arrow in tunnal[pipe[move[0]][move[1]]-1]:
        runn = move[:]
        runn[0] += arrow[0]
        runn[1] += arrow[1]
        if 0 <= runn[0] < N and 0 <= runn[1] < M:
            if pipe[runn[0]][runn[1]] != 0:
                if [move[0]-runn[0],move[1]-runn[1]] in tunnal[pipe[runn[0]][runn[1]] - 1]:
                    running.append([runn[0],runn[1]])
                    tunnal_map[runn[0]][runn[1]] = 1
    # for a in range(N):
    #     print(tunnal_map[a],pipe[a])
    # print()
    for go in range(2,L):
        move = running[:]
        running = []
        for mov in move:
            for arrow in tunnal[pipe[mov[0]][mov[1]]-1]:
                runn = mov[:]
                runn[0] += arrow[0]
                runn[1] += arrow[1]
                if 0 <= runn[0] < N and 0 <= runn[1] < M:
                    if pipe[runn[0]][runn[1]] != 0:
                        if [mov[0] - runn[0], mov[1] - runn[1]] in tunnal[pipe[runn[0]][runn[1]] - 1]:
                            running.append([runn[0],runn[1]])
                            tunnal_map[runn[0]][runn[1]] = 1
        # for a in range(N):
        #     print(tunnal_map[a],pipe[a])
        # print()
    total = 0
    for k in range(len(tunnal_map)):
        total += tunnal_map[k].count(1)
    print('#{0} {1}'.format(test_case,total))
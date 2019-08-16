T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    person = []
    for i in range(M):
        person.append(list(map(int, input().split())))
    town = []
    for men in person:
        if len(town) == 0:
            town.append(men)
        for i in range(len(town)):
            if men[0] in town[i] or men[1] in town[i]:
                town[i].extend(men)
                town[i] = list(set(town[i]))
            elif i == len(town)-1:
                town.append(men)
    towns = [0]*len(town)
    for i, j in enumerate(town):
        if i == 0 :
            continue
        for a in range(len(town)):
            if a != i:
                for num in j:
                    if num in town[a]:
                        town[a].extend(j)
                        town[a] = list(set(town[a]))
                        towns[i] = 1
                        break
    for i in range(len(towns)-1, -1, -1):
        if towns[i] == 1:
            del town[i]
    members = [1]*N
    for j in town:
        for i in j:
            members[i-1] = 0
    for i, j in enumerate(members, 1):
        if j == 1:
            town.append([i])
    print('#{} {}'.format(test_case, len(town)))
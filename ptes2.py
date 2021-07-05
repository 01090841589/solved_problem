import sys
sys.setrecursionlimit(10000)


answer = 0
def solution(N,K,T):
    global answer

    def reserve(dat, scr):
        global answer
        if answer == N or answer >= K-dat+scr:
            return
        if scr == N:
            answer = scr
            return
        if dat == K:
            answer = max(answer, scr)
            return
        for stu in summit[dat]:
            if answer == N or answer >= K - dat + scr:
                return
            if student[stu]:
                student[stu] = 0
                reserve(dat+1, scr+1)
                student[stu] = 1
        reserve(dat+1, scr)

    summit = [[] for _ in range(K)]
    student = [1] * N
    dummy = 0
    for i in range(N):
        if T[i][0] == 1 and T[i][1] == K:
            dummy += 1
            N -= 1
            continue
        for j in range(T[i][0]-1, T[i][1]):
            summit[j].append(i)
    summit.sort(key=len)
    skip, ress = 0, 0
    for i in range(K):
        if not summit[i]:
            skip += 1
        if len(summit[i]) == 1:
            if student[summit[i][0]] == 1:
                student[summit[i][0]] = 0
                skip += 1
                ress += 1
            else:
                skip += 1

    # summit[skip:].sort(key=lambda x:x[0])
    reserve(skip, ress)
    if answer < K:
        if answer+dummy > K:
            answer = K
        else:
            answer += dummy
    return answer



# print(solution(4, 4, [[1, 3], [1, 1], [2, 3], [3, 4]]))
# print(solution(100, 100, [[1, 2], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100], [1, 100]]))
# print(solution(4, 10, [[2, 3], [2, 3], [3, 5], [2, 3]]))




# def solution(n, v1, v2, num, amount):
#     visited = [-1] * (n+1)
#     scr = [0] * (n+1)
#     groups = []
#     for i in range(len(v1)):
#         groups.append([min(v1[i], v2[i]), max(v1[i], v2[i])])
#
#     groups.sort(key= lambda x:x[1])
#     groups.sort()
#
#     for i in range(len(v1)):
#         l, r  = groups[i][0], groups[i][1]
#         if visited[l] == -1 and visited[r] == -1:
#             visited[r] = l
#         else:
#             if visited[l] == -1:
#                 visited[l] = visited[r]
#             elif visited[r] == -1:
#                 visited[r] = visited[l]
#             else:
#                 L = l
#                 while True:
#                     if visited[L] == -1:
#                         break
#                     else:
#                         L = visited[L]
#                 R = r
#                 while True:
#                     if visited[R] == -1:
#                         break
#                     else:
#                         R = visited[R]
#                 if L > R:
#                     visited[L] = R
#                 elif R > L:
#                     visited[R] = L
#
#
#     for i in range(len(num)):
#         l, r = num[i], amount[i]
#         while True:
#             if visited[l] == -1:
#                 scr[l] += r
#                 break
#             else:
#                 l = visited[l]
#
#     answer = 0
#     grade = -9999
#
#     for i in range(1, n+1):
#         if visited[i] == -1 and scr[i] > grade:
#             grade = scr[i]
#             answer = i
#     return answer



# solution(10,	[1, 10, 6, 5, 6, 9],	[3, 7, 2, 8, 7, 3],	[3, 4, 5, 1, 8, 7, 9, 2],	[10, 5, 6, -6, -8, 2, -2, 5])
# solution(6, [1, 5, 3, 6, 2], [5, 4, 6, 2, 3], [1, 5, 4, 3, 6, 2], [3, 6, -2, 2, 2, 2])

# print(solution(	8,
#                    [1, 3, 5, 7, 1, 4, 1],
#                    [2, 4, 6, 8, 7, 5, 6],
#                    [2, 2, 3],
#                    [2, -2, 1]))



#
# def solution(N, mine):
#     answer = [[0] * N for _ in range(N)]
#     DIR = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
#     for mi in mine:
#         answer[mi[0]-1][mi[1]-1] = -1
#
#     for mi in mine:
#         y = mi[0]-1
#         x = mi[1]-1
#         for c in DIR:
#             Y = y+c[0]
#             X = x+c[1]
#             if 0 <= Y < N and 0 <= X < N:
#                 if answer[Y][X] >=0:
#                     answer[Y][X] += 1
#
#
#     [print(answer[i]) for i in range(N)]
#     return answer
#
# solution(9,	[ [1, 1], [1, 7], [2, 7], [3, 6], [4, 1], [4, 4], [4, 8], [8, 4], [8, 5], [9, 6] ])
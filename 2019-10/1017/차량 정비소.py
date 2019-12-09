import sys
sys.stdin = open("차량정비소.txt")


from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    a1 = list(map(int, input().split()))
    b1 = list(map(int, input().split()))
    people = list(map(int, input().split()))
    reception = [0]*N
    rapait = [0]*M
    scr = 0
    a2 = [[0, 0, 0, 0] for _ in range(N)]
    b2 = [[0, 0, 0, 0] for _ in range(M)]

    visited = []
    time = 0
    nums = 1
    wait = []
    # print(N, M, K, A, B)
    # print(a2, b2, people)
    for i in range(1000):
        for i in range(N):
            if a2[i][2] > 0:
                a2[i][2] -= 1
        for i in range(M):
            if b2[i][2] > 0:
                b2[i][2] -= 1

        for i in range(N):
            if a2[i][2] == 0 and a2[i][1] != 0:
                wait.append([a2[i][0], a2[i][1], a2[i][2], i])
                a2[i] = [0, 0, 0, 0]
                if people:
                    a2[i][0] = people.pop(0)
                    a2[i][1] = nums
                    nums += 1
                    a2[i][2] = a1[i]
            elif a2[i][2] == 0 and people:
                a2[i][0] = people.pop(0)
                a2[i][1] = nums
                nums += 1
                a2[i][2] = a1[i]

        for i in range(M):
            if b2[i][2] == 0 and b2[i][1] == 0 and wait:
                b2[i][0] = wait[0][0]
                b2[i][1] = wait[0][1]
                b2[i][2] = b1[i]
                b2[i][3] = wait[0][3]
                wait.pop(0)
            elif b2[i][2] == 0 and b2[i][1] != 0:
                visited.append([b2[i][0], b2[i][1], b2[i][3], i])
                b2[i] = [0, 0, 0, 0]
                if wait:
                    b2[i][0] = wait[0][0]
                    b2[i][1] = wait[0][1]
                    b2[i][2] = b1[i]
                    b2[i][3] = wait[0][3]
                    wait.pop(0)

        time += 1
        # print(a2, b2, people, visited, wait, time)
    result = 0
    for i in range(K):
        if visited[i][2] == (A-1) and visited[i][3] == (B-1):
            result += visited[i][1]
    print(result)
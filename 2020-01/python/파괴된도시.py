import sys
sys.stdin = open('18231_input.txt')

import sys
sys.setrecursionlimit(10**6)
def printSet(target):
    print(result)
    for i in range(len(target)):
        print('%d' % target[i], end=' ')
    print()

def check_city(n):
    global flag, result

    # (주어진 지도)파괴된 도시의 번호에 1 표시
    destroyed_city = [0] * (N + 1)
    for i in data:
        destroyed_city[i] = 1
    # print(destroyed_city)

    # 부분 집합으로 뽑은 도시 번호 Q에 담기
    Q = []
    for i in range(n):
        if A[i] == 1:
            Q.append(city[i])
    # print(Q)

    # 내가 뽑은 도시랑 주어진 지도랑 비교해서 파괴 or 그만
    for i in Q:
        if destroyed_city[i] >= 1 and destroyed_city_original[i] == 1:
            destroyed_city[i] += 1
            for j in range(len(connect_info[i])):
                if connect_info[i][j] == 1:
                    destroyed_city[j] += 1
        elif destroyed_city[i] == 0 and destroyed_city_original[i] == 0:
            break


    cnt = 0
    for i in range(1, len(destroyed_city_original)):
        if destroyed_city_original[i] == 0 and destroyed_city[i] == 0:
            cnt += 1
        elif destroyed_city_original[i] == 1 and destroyed_city[i] >= 2:
            cnt += 1

    if cnt == N:
        flag = 0
        if flag == 0 and result == -1:
            result = len(Q)
            printSet(Q)


def powerset(n, k, t):
    if t > K:
        return

    if n == k:
        check_city(n)

    else:
        A[k] = 1
        powerset(n, k+1, t + sum(connect_info[k]) + 1)
        A[k] = 0
        powerset(n, k+1, t)

# N개의 도시, M개의 도로
N, M = map(int, input().split())

# 연결 정보
connect_info = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    temp = list(map(int, input().split()))
    connect_info[temp[0]][temp[1]] = connect_info[temp[1]][temp[0]] = 1

# [print(connect_info[i]) for i in range(len(connect_info))]
# K 파괴된 도시의 개수
K = int(input())

# 파괴된 도시 번호 리스트
data = list(map(int, input().split()))

# 파괴된 도시의 번호에 1 표시
destroyed_city_original = [0] * (N + 1)
for i in data:
    destroyed_city_original[i] = 1

# 부분집합 준비
city = [i for i in range(1, N+1)]
A = [0] * N

flag = 1
result = -1

while flag:
    powerset(N, 0, 0)

    if result == -1:
        flag = 0
        print(result)
    else:
        break
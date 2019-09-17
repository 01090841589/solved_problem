import sys
sys.stdin = open('양팔.txt')

def kgs(N, visited, k, left):
    # if sum(right) > sum(left):
    #     return
    if N == k:
        if len(left) == 3:
            # print(left)
            return
    else:
        for i in range(N):
            if visited[i] == 1:
                continue
            visited[i] = 1
            kgs(N, visited, k+1, left+str(weight[i]))
            visited[i] = 0
            kgs(N, visited, k+1, left)


T = int(input())
for tc in range(1, 4):
    N = int(input())
    weight = list(map(int, input().split()))
    print(weight)
    for i in range(1):
        kgs(N, [0]*N, 0, '')
        weight.append(weight.pop(0))
import sys
sys.stdin = open("평범한배낭.txt")

def knapsack():
    global KS, N, K, weight, value
    for i in range(N+1):
        KS[i][0] = 0
    for K in range(K+1):
        KS[0][K] = 0

    for i in range(1, N+1):
        for K in range(1, K+1):
            if weight[i] > K:
                KS[i][K] = KS[i-1][K]
            else:
                KS[i][K] = max(KS[i-1][K-weight[i]]+value[i], KS[i-1][K])


N, K = map(int, input().split())
KS = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
weight = [0 for _ in range(N+1)]
value = [0 for _ in range(N+1)]
for n in range(1, N+1):
    weight[n], value[n] = map(int, input().split())
knapsack()
print(KS[N][K])
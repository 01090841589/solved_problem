a = [1, 2, 3, 4, 5, 6]
N = len(a)


def comb(k, n, visited):
    if k == n:
        print(visited)
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        comb(k+1, n, visited)
        visited[i] = 0


comb(0, 3, [0]*N)
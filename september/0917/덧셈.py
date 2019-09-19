

def summ(k, scr):
    if scr == num:
        result = []
        for j in range(N):
            if visited[j]:
                result.append(j+1)
        print(result)
        return
    if scr > num:
        return
    if k >= N:
        return
    visited[k] = arr[k]
    summ(k+1, scr+arr[k])
    visited[k] = 0
    summ(k+1, scr)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
num = 10
visited = [0] * N
summ(0, 0)
arr = [0,5,4,0,6,0]

def perm(k, n):
    global result
    if k == N:
        babyGin(n)
        return
    if result == 1:
        return
    for i in range(N):
        if visited[i] == 1:
            continue
        visited[i] = 1
        perm(k+1, n+[arr[i]])
        visited[i] = 0


def babyGin(n):
    global result
    flag = 0
    if n[0]==n[1]==n[2] or n[0]+1 == n[1] == n[2]-1:
        flag += 1
    if n[3] == n[4] == n[5] or n[3] + 1 == n[4] == n[5] - 1:
        flag += 1
    if flag == 2:
        result += 1
        return
N = len(arr)
result = 0
visited = [0]*6
perm(0, [])
if result:
    print('babygin')
else:
    print('none')
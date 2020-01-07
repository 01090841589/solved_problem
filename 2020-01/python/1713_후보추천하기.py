import sys
sys.stdin = open("후보추천하기.txt")

N = int(input())
M = int(input())

rec = list(map(int, input().split()))
post = [[0, 0] for _ in range(N)]
first, num = 0, 0
for i in range(M):
    flag = 1
    for j in range(N):
        if post[j][1] == 0:
            continue
        elif rec[i] == post[j][1]:
            flag = 0
            num = j
            break
    if flag:
        post.sort(key=lambda k:k[0])
        post[0][0] = 10000+(i+1)
        post[0][1] = rec[i]
    else:
        post[num][0] += 10000
        pass
post.sort(key=lambda k:k[1])
for i in range(N):
    if post[i][1] != 0:
        print(post[i][1], end=' ')
print()
print(post)
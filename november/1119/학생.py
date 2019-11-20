import sys
sys.stdin = open("학생.txt")

from collections import deque

def plus(n):
    global res
    if n == N-1:
        return
    for i in range(21):
        if visited[n][i] > 0:
            if i+nums[n] < 21:
                visited[n+1][i+nums[n]] += visited[n][i]
            if i-nums[n] >= 0:
                visited[n+1][i-nums[n]] += visited[n][i]
    plus(n+1)



N = int(input())
nums = list(map(int, input().split()))
result = nums.pop()
visited = [[0]*21 for _ in range(N)]
res = 0
visited[1][nums[0]] = 1
plus(1)
print(visited[N-1][result])
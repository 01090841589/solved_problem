import sys
sys.stdin = open("13975.txt")

import heapq
T = int(input())
for tc in range(T):
    N = int(input())
    files = list(map(int, input().split()))
    h_files = []
    res = 0
    for file in files:
        heapq.heappush(h_files, file)
    while len(h_files) > 2:
        left = heapq.heappop(h_files)
        right = heapq.heappop(h_files)
        res += left+right
        heapq.heappush(h_files, left+right)
    print(res+sum(h_files))
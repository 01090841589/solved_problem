import sys
sys.stdin = open('최소스패닝.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    [print(nodes[i]) for i in range(E)]
    visited = [[0] * (E+1) for _ in range(E+1)]
    for node in nodes:
        visited[node[0]][node[1]] = node[2]
    [print(visited[i]) for i in range(E+1)]

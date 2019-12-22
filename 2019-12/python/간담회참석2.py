import sys
sys.stdin = open("간담회참석.txt")

import heapq

def daijxtra(graph, starting_vertex):
    distances = {vertex: 1234567891 for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances


T = int(input())
for tc in range(1, T+1):
    N, M, G = map(int, input().split())
    node1 = { i : {} for i in range(1, N+1)}
    node2 = { i : {} for i in range(1, N+1)}
    for _ in range(M):
        v, e, g = map(int, input().split())
        node1[v][e] = g
        node2[e][v] = g
    result1 = daijxtra(node1, G)
    result2 = daijxtra(node2, G)
    for i in range(1, N+1):
        result1[i] += result2[i]
    print('#{} {}'.format(tc, max(result1.values())))
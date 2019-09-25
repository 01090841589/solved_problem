def times(k, way, N, node, cook_times, play):
    win = 0
    for i in range(1, N+1):
        if node[k][i]:
            way.append(i)
            play[i] = 1
    while way:
        a = way.pop()
        how = times(a, [], N, node, cook_times, play)
        if win < how:
            win = how
    return cook_times[k-1]+win
def solution(cook_times, order, k):
    print(cook_times, order, k)
    N = len(cook_times)
    node = [[0] * (N+1) for _ in range(N+1)]
    for a in order:
        node[a[1]][a[0]] = 1
    visited = [0]*(N+1)
    result = times(k, [], N, node, cook_times, visited)
    return [visited.count(1), result]

print(solution([5, 30, 15, 30, 35, 20, 4], [[2, 4],[2, 5], [3, 4], [3, 5], [1, 6], [4, 6], [5, 6], [6, 7]], 1))
print(solution([5, 30, 15, 30, 35, 20, 4], [[2, 4],[2, 5], [3, 4], [3, 5], [1, 6], [4, 6], [5, 6], [6, 7]], 2))
print(solution([5, 30, 15, 30, 35, 20, 4], [[2, 4],[2, 5], [3, 4], [3, 5], [1, 6], [4, 6], [5, 6], [6, 7]], 3))
print(solution([5, 30, 15, 30, 35, 20, 4], [[2, 4],[2, 5], [3, 4], [3, 5], [1, 6], [4, 6], [5, 6], [6, 7]], 4))
print(solution([5, 30, 15, 30, 35, 20, 4], [[2, 4],[2, 5], [3, 4], [3, 5], [1, 6], [4, 6], [5, 6], [6, 7]], 5))
print(solution([5, 30, 15, 30, 35, 20, 4], [[2, 4],[2, 5], [3, 4], [3, 5], [1, 6], [4, 6], [5, 6], [6, 7]], 6))
print(solution([5, 30, 15, 30, 35, 20, 4], [[2, 4],[2, 5], [3, 4], [3, 5], [1, 6], [4, 6], [5, 6], [6, 7]], 7))

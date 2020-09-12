from collections import deque
def solution(n, s, a, b, fares):
    def after_double(k, scr):
        now_size = [999999] * ( n+ 1)
        now_size[k] = 0
        q = deque()
        q.append([k, size[k]])
        while q:
            now = q.popleft()
            for i in MAP2[now[0]]:
                if now_size[i] > now_size[now[0]] + MAP[now[0]][i]:
                    now_size[i] = now_size[now[0]] + MAP[now[0]][i]
                    q.append([i, now_size[now[0]] + MAP[now[0]][i]])

        if scr > now_size[a]+ now_size[b] + size[k]:
            return now_size[a]+ now_size[b] + size[k]
        else:
            return scr

    answer = 0
    scr = 9999999
    MAP = [[0] * (n+1) for _ in range(n+1)]
    MAP2 = [[] * (n+1) for _ in range(n+1)]
    size = [999999] * (n+ 1)
    size[s] = 0
    for node in fares:
        MAP[node[0]][node[1]] = node[2]
        MAP[node[1]][node[0]] = node[2]
        MAP2[node[0]].append(node[1])
        MAP2[node[1]].append(node[0])
    q = deque()
    q.append([s, 0])
    while q:
        now = q.popleft()
        for i in MAP2[now[0]]:
            if size[i] > size[now[0]] + MAP[now[0]][i]:
                size[i] = size[now[0]] + MAP[now[0]][i]
                q.append([i, size[now[0]] + MAP[now[0]][i]])
    scr = size[a] + size[b]

    for i in range(1, n+1):
        if size[i] != 0:
            scr = after_double(i, scr)
    answer = scr
    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
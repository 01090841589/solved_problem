def solution(flowers):
    answer = 0
    start = 365
    end = 0
    days = [0 for _ in range(366)]
    for flower in flowers:
        for day in range(flower[0], flower[1]):
            days[day] += 1
        if start > flower[0]:
            start = flower[0]
        if end < flower[1]:
            end = flower[1]
    for i in range(start, end):
        if days[i]:
            answer += 1
    return answer

print(solution([[3, 4],[4, 5], [6, 7], [8, 10]]))
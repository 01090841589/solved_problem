answer = 0
def solution(k):
    global answer
    def matches(t, scr, site):
        global answer
        if t == 0:
            answer += scr
            return
        if site == 0:
            if t == 6:
                answer += 1
            for i in first:
                if t >= i[0]:
                    matches(t-i[0], scr*i[1], site+1)
                else:
                    return
        else:
            for i in other:
                if t >= i[0]:
                    matches(t-i[0], scr*i[1], site+1)
                else:
                    return
    first = [[2, 1], [3, 1], [4, 1], [5, 3], [6, 2], [7, 1]]
    other = [[2, 1], [3, 1], [4, 1], [5, 3], [6, 3], [7, 1]]
    matches(k, 1, 0)

    return answer

print(solution(11))
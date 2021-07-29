def solution(places):
    DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    def search_people(y, x, k):
        if k == 0:
            return
        for c in DIR:
            Y, X = y+c[0], x+c[1]
            if 0 <= Y < 5 and 0 <= X < 5 and not visited[Y][X]:
                if place[Y][X] == "O":
                    search_people(Y, X, k-1)
                elif place[Y][X] == "P":
                    find[0] = 0


    answer = []
    for place in places:
        find = [1]

        visited = [[0] * 5 for _ in range(5)]
        for y in range(5):
            for x in range(5):
                if place[y][x] == "P":
                    visited[y][x] = 1
                    search_people(y, x, 2)
                if not find[0]:
                    break
        answer.append(find[0])
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
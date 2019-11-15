import sys
sys.stdin = open("조각움직이기")


from itertools import permutations, combinations
from collections import deque

DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def train(y, x, n):
    k = 1
    pin[y][x] = 2
    queue = deque()
    queue.append([y, x])
    while queue:
        [y, x] = queue.popleft()
        if k == n:
            return True
        for c in DIR:
            Y = y+c[0]
            X = x+c[1]
            if 0 <= Y < 5 and 0 <= X < 5 and pin[Y][X] == 1:
                if [Y, X] in visited:
                    pin[Y][X] = 2
                    queue.append([Y, X])
                    k += 1

    return False



MAP = [list(input()) for _ in range(5)]
now = []
for y in range(5):
    for x in range(5):
       if MAP[y][x] == '*':
           now.append([y, x])
result = 5 * 5 * len(now)


for dots in combinations(range(0, 25), len(now)):
    visited = []
    pin = [[0] * 5 for _ in range(5)]
    for dot in dots:
        visited.append([dot//5,dot % 5])
        pin[dot//5][dot % 5] = 1
    if train(visited[0][0], visited[0][1], len(now)):
        for lend in permutations(range(0, len(now)), len(now)):
            scr = 0
            for i in range(len(now)):
                scr += abs(visited[i][0]-now[lend[i]][0])+abs(visited[i][1]-now[lend[i]][1])
            if result > scr:
                result = scr
print(result)
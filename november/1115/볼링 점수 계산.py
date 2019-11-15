import sys
sys.stdin = open("볼링점수계산.txt")

balling = input()
turns = [0]*15
scores = [[0, 0] for _ in range(15)]
turn = 0
first = 0
buf = 0
score = 0
for i, j in enumerate(balling):
    if j != "S" and j != "P" and j != "-":
        if first == 0:
            buf = int(j)
            scores[turn][first] = buf
            first = 1
        else:
            scores[turn][first] = scores[turn][0]+int(j)
            turn += 1
            buf = 0
            first = 0
    elif j == "S":
        scores[turn][first] = 10
        turns[turn] = 2
        turn += 1
        buf = 0
        first = 0
    elif j == "P":
        scores[turn][first] = 10
        turns[turn] = 1
        turn += 1
        buf = 0
        first = 0
    elif j == "-":
        if first == 1:
            scores[turn][first] = scores[turn][0]
            turn += 1
            buf = 0
            first = 0
        else:
            first = 1

for i in range(9):
    if scores[i][1] == 10:
        score += 10
        score += scores[i+1][0]
    elif scores[i][0] == 10:
        score += 10
        if scores[i+1][0] == 10:
            score += 10
            score += scores[i+2][0]
        else:
            score += scores[i+1][1]
    else:
        score += max(scores[i][0], scores[i][1])


for i in range(9, 12):
    score += max(scores[i][0], scores[i][1])
print(score)
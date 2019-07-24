from itertools import combinations
T = 2
N = 3
score = [2, 3, 5]
list(combinations)
for i in range(len(score)):
    for j in range(i+1, len(score)):
        print(i, j)
for i in range(len(score)):
    for j in range(i+1, len(score)):
        for k in range(j+1, len(score)):
            print(i, j, k)
for i in range(len(score)):
    for j in range(i+1, len(score)):
        for k in range(j+1, len(score)):
            for l in range(k+1, len(score)):
                print(i, j, k, l)

add = []
for i in range(1, len(score)+1): #원소 1개부터 전체까지 지정
    add.append(1)
    for j in range(1, len(add)+1):
        [j]

for add[i] in range(len(score)):
    for add[j] in range(i+1, len(score)):
        for add[k] in range(j+1, len(score)):
            for add[l] in range(k+1, len(score)):
                print(i, j, k, l)
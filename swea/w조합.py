import itertools



n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66]

for i in itertools.permutations(n):
    print(i)
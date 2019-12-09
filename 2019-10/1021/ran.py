import random

A, B, C = 50, 50, 50

# for i in range(A):
#     a = random.sample(list(range(3, A+10)), B)
#     a = list(map(str, a))
#     print(' '.join(a))
#
# for i in range(C):
#     q = random.sample(list(range(2, A)), 1)
#     w = random.sample(list(range(2)), 1)
#     e = random.sample(list(range(2, C)), 1)
#     print('{} {} {}'.format(q[0], w[0], e[0]))

for i in range(10):
    for j in range(10):
        print(random.randrange(1,6), end=' ')
    print()
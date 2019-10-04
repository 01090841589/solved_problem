import sys
sys.stdin = open("로또.txt")


from itertools import combinations


while True:
    num = list(map(int, input().split()))
    result = []
    visited = [0] * num[0]
    if num == [0]:
        break
    for a in combinations(num[1:], 6):
        print("{} {} {} {} {} {}".format(a[0], a[1], a[2], a[3], a[4], a[5]))
    print()
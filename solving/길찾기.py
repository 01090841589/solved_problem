# 0 1 0 2 1 4 1 3 4 8 4 3 2 9 2 5 5 6 5 7 7 99 7 9 9 8 9 10 6 10 3 7
import copy
A = list(map(int,input().split()))
print(A)
route = [[0]]
comp_route = copy.deepcopy(route)
for a in comp_route:
    print(a)
    jump = a[-1]
    route.remove(a)
    for i in range(len(A)):
        if i % 2 == 0:
            if A[i] == jump:
                print(a)
                a.append(A[i+1])
    if len(a) > 0:
        route.append(a)
print(route)
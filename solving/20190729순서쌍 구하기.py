from itertools import permutations
right = []
left = []
n = [1, 2, 4]
cnt = 0
total = []
N =list(permutations(n,len(n)))
print(N)
for i,j in enumerate(N,1):
    print(j)
    for a,b in enumerate(j):
        for c, d in enumerate(list(permutations(n,a))):
            right = list(j)
            left = []
            for num in d:
                left.append(num)
                right.remove(num)
            if sum(left) < sum(right):
                cnt += 1
                print('r이큼',end='')
            print(right,left,end='   ')
            print(d,end='')
            print(sum(d),end='')
        print()
print(cnt)
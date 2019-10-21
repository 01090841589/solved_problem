import sys
sys.stdin = open("lcs.txt")

def lcs(a, b):
    prev = [0]*len(a)
    for i,r in enumerate(a):
        current = []
        for j,c in enumerate(b):
            if r==c:
                e = prev[j-1]+1 if i* j > 0 else 1
            else:
                e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)  
            current.append(e)
        prev = current
    k = 1
    print(current)
    for i in range(len(a)):
        if current[i] == k:
            result.append(A[current[i]])
            k += 1
    return current[-1]

A = input()
B = input()
result = []
print(lcs(A, B))
print(result)
import sys
sys.stdin = open("캠핑.txt")

T = 1
while True:
    L, P, V = map(int, input().split())
    if L==0 and P==0 and V==0:
        break
    result = (V//P)*L+min(V%P, L)
    print('Case {}: {}'.format(T, result))
    T+=1
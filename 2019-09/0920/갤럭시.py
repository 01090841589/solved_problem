import sys
sys.stdin = open("갤럭시.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int,input().split()))
    result = 0
    while N > 1:
        print(C)
        min_lst = []
        for i in range(N-1):
            min_lst.append(C[i]+C[i+1])
        a = min_lst.index(min(min_lst))
        b = C.pop(a)+C.pop(a)
        C.insert(a, b)
        result += b
        N -= 1

    print(result)
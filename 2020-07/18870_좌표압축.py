import sys
sys.stdin = open("18870.txt")

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    res = 0
    flag = 0
    for num in A:
        if num <= B[flag]:
            res += B[flag]
        else:
            bf = flag
            buf = abs(num - B[flag])
            bf += 1
            while True:
                if num <= B[bf]:
                    if (B[bf] - num) < buf:
                        res += B[bf]
                        if bf > flag:
                            flag = bf-1
                        break
                    else:
                        res += B[bf-1]
                        if bf > flag:
                            flag = bf-1
                        break
                else:
                    buf = abs(num - B[bf])
                if bf == (len(B)-1):
                    res += B[bf]
                    break
                bf += 1
    print(res)
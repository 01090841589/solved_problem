import sys
sys.stdin = open("덧셈문제.txt")

T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    if N > 1:
        print(((B*(N-2))-(A*(N-2)))+1)
    elif N == 1:
        if A == B:
            print(1)
        else:
            print(0)
    else:
        print(0)
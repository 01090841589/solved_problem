import sys
sys.stdin = open("수열편집.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    command = [list(map(str, input().split())) for _ in range(M)]
    for com in command:
        if com[0] == 'I':
            arr.insert(int(com[1]), int(com[2]))
        elif com[0] == 'D':
            del arr[int(com[1])]
        elif com[0] == 'C':
            arr[int(com[1])] = int(com[2])
    try:
        print('#{} {}'.format(tc, arr[L]))
    except:
        print('#{} -1'.format(tc))

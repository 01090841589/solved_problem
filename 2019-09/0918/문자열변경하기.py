import sys
sys.stdin = open("문자열변경하기.txt")
import time
start_time = time.time()

T = int(input())
for tc in range(1, T+1):
    start = time.time()
    S = list(input())
    T = list(input())
    N = len(S)
    cnt = 0
    ab = T[0]
    Sab = []
    Tab = []
    for i in range(N):
        if S[i] == T[0]:
            Sab.append(i)
        if T[i] == T[0]:
            Tab.append(i)
    for i in range(len(Sab)):
        cnt += abs(Sab[i]-Tab[i])
    print('#{} {}'.format(tc, cnt))

end_time = time.time()
print("WorkingTime: {} sec".format(end_time-start_time))
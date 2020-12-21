import sys
sys.stdin = open("1079.txt")

def mafia(k, crime, men, day):
    global res
    if k == N:
        print(k, crime)
        return
    if men % 2:
        #낮
        kill_crime = crime[:]
        minc, minn = -1, -1
        for i in range(N):
            if minc < kill_crime[i] and kill_crime[i] > 0:
                minc = kill_crime[i]
                minn = i
        if minn == you:
            if res < day:
                res = day
            return
        kill_crime[minn] = -1

        mafia(k+1, kill_crime, men-1, day)

    else:
        #밤
        buf = -1
        for i in range(N):
            kill_crime = crime[:]
            if kill_crime[i] > 0 and i != you:
                kill_crime[i] = -1
                for j in range(N):
                    if kill_crime[j] > 0:
                        kill_crime[j] += MAP[i][j]
                mafia(k+1, kill_crime, men-1, day+1)
res = 0
N = int(input())
crime = list(map(int, input().split()))
MAP = [list(map(int, input().split())) for _ in range(N)]
you = int(input())

mafia(0, crime[:], N, 0)
print(res)
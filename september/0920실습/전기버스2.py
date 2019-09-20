import sys
sys.stdin = open("전기버스2.txt")

def charge(n, battery, rest, visited):
    global N, result
    if result < rest:
        return
    if battery < 0 and n > 0 :
        return
    if n == N-1:
        if result > rest:
            result = rest
        return
    if battery > 0:
        charge(n+1, battery-1, rest, visited)
    battery = bus_stop[n]
    rest += 1
    visited[n] = 1
    charge(n+1, battery-1, rest, visited)


T = int(input())
for tc in range(1, T+1):
    bus_stop = list(map(int, input().split()))
    bus_stop.append(0)
    N = bus_stop.pop(0)
    result = N
    visited = [0]*N
    charge(0, 0, -1, [0]*N)
    if result == N:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, result))
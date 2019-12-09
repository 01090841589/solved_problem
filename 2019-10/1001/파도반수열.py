


N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort()
times = sorted(times, key=lambda a: a[1])
result = 0
buf = 0
for i in range(N):
    if buf == 0:
        buf = times[i][1]
        print(times[i])
        result += 1
    else:
        if times[i][0] >= buf:
            result += 1
            print(times[i])
            buf = times[i][1]
print(times)
print(result)
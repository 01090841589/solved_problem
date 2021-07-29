
result = 0
def solution(play_time, adv_time, logs):
    def doke(k, visited, scr):
        global result
        if k == N:
            if result < scr:
                result = scr
            return
        if scr + (max_time - times[k][1]) <= result:
            return
        flag = 1
        for i in range(times[k][0], times[k][1]):
            if visited[i] != 0:
                flag = 0
                break
        if flag:
            visits = visited[:]
            for i in range(times[k][0], times[k][1]):
                visits[i] = 1
            doke(k + 1, visits, scr + 1)
        doke(k + 1, visited, scr)
    times = []
    max_time = 0
    for log in logs:
        start = int(log[:2])*60*60 + int(log[3:5])*60 + int(log[6:8])
        end = int(log[9:11])*60*60 + int(log[12:14])*60 + int(log[15:17])
        times.append([start, end])
        max_time = max(max_time, end)
    N = len(times)
    times = sorted(times, key=lambda times: times[1])
    print(times)
    play = int(play_time[:2])*60*60 + int(play_time[3:5])*60 + int(play_time[6:8])
    adv = int(adv_time[:2])*60*60 + int(adv_time[3:5])*60 + int(adv_time[6:8])
    print(adv, max_time)
    doke(adv, [0]*max_time, 0)
    print(result)

    answer = ''
    return answer

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))

def solution(lines):
    answer = 1
    start = 24*60*60+2
    end = 0
    time_lines = []
    num = 1
    lists = []
    for li in lines:
        time = li.split(' ')
        hour, min, sec, traf = int(time[1][:2])*1000*3600, int(time[1][3:5])*1000*60, int(time[1][6:8]+time[1][9:12]), time[2][:-1]
        traf_sec = traf.split('.')
        if len(traf_sec) == 1:
            traf_sec = [traf_sec[0], '000']
        if len(traf_sec[1])<3:
            traf_sec[1] = traf_sec[1].ljust(3, '0')
        traf = int(traf_sec[0]+traf_sec[1])
        end_traf = (hour+min+sec)
        ago_traf = hour+min+sec - (traf-1)
        if ago_traf > 0 :
            time_lines.append([ago_traf, 0, num])
            time_lines.append([end_traf+999, 1, num])
        else:
            lists.append(num)
            time_lines.append([end_traf+999, 1, num])
        num += 1
    answer = len(lists)
    time_lines.sort()
    for i in range(len(time_lines)):
        if time_lines[i][2] in lists:
            lists.remove(time_lines[i][2])
        else:
            lists.append(time_lines[i][2])
            if answer < len(lists):
                answer = len(lists)
    return answer
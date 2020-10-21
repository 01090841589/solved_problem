def solution(dartResult):
    answer = 0
    scr = [0] * 3
    scr_buf = ''
    scr_num = 0
    for order in dartResult:
        if '0' <= order <= '9':
            scr_buf += order
        elif order == 'S':
            scr[scr_num] = int(scr_buf)
            scr_num += 1
            scr_buf = ''
        elif order == 'D':
            scr[scr_num] = int(scr_buf) ** 2
            scr_num += 1
            scr_buf = ''
        elif order == 'T':
            scr[scr_num] = int(scr_buf) ** 3
            scr_num += 1
            scr_buf = ''
        elif order == '*':
            scr[scr_num-1] *= 2
            if scr_num-2 > -1:
                scr[scr_num-2] *= 2
        elif order == '#':
            scr[scr_num-1] *= -1
    answer = sum(scr)
    return answer
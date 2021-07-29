def solution(n, k, cmd):
    answer = ''
    chart = [0] * n
    cs = k
    stacks = []
    for cm in cmd:
        if cm[0] == "U":
            cnt = sum(chart[cs-int(cm[1:])+1:cs+1])
            cs -= (int(cm[1:]))
            while True:
                if chart[cs] == 1:
                    cs -= 1
                else:
                    break
            while cnt > 0:
                if chart[cs-1] == 0:
                    cnt -= 1
                cs -= 1
        elif cm[0] == "D":
            cnt = sum(chart[cs:cs+int(cm[1:])])
            cs += (int(cm[1:]))
            while True:
                if chart[cs] == 1:
                    cs += 1
                else:
                    break
            while cnt > 0:
                if chart[cs+1] == 0:
                    cnt -= 1
                cs += 1
        elif cm[0] == "C":
            stacks.append(cs)
            chart[cs] = 1
            flag = 0
            for i in range(1, 5000):
                if cs+i < n:
                    if chart[cs+i] == 0:
                        cs += i
                        flag = 1
                        break
                else:
                    break
            if flag:
                continue
            if sum(chart[cs:]) == n-cs:
                while True:
                    cs -= 1
                    if chart[cs] == 0:
                        break
            else:
                cs += 5000
                while True:
                    cs += 1
                    if chart[cs] == 0:
                        break
        else:
            chart[stacks.pop()] = 0
    for i in chart:
        if i:
            answer += "X"
        else:
            answer += "O"
    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
# print(solution(10, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
print(solution(1000000, 2, ["D 200000","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","U 11999","C","U 8188","D 11888", "U 11888", "C","U 11888","C","U 11188","C","C"]))
# OOOXXOOOOO
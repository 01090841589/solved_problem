answer = 0
flag = 0
def solution(t1, t2):
    global flag, answer
    def cor_tree(num, t2_num):
        global flag, anmswer
        if flag:
            return
        if t1[num][0] > 0 and t2[t2_num][0] > 0:
            cor_tree(t1[num][0], t2[t2_num][0])
        elif t1[num][0] > 0 and t2[t2_num][0] == -1:
            flag = 1
            return
        elif t1[num][0] == -1 and t2[t2_num][0] > 0:
            flag = 1
            return
        if t1[num][1] > 0 and t2[t2_num][1] > 0:
            cor_tree(t1[num][1], t2[t2_num][1])
        elif t1[num][1] > 0 and t2[t2_num][1] == -1:
            flag = 1
            return
        elif t1[num][1] == -1 and t2[t2_num][1] > 0:
            flag = 1
            return

    max_len = len(t1)
    max_len2 = len(t2)
    for i in range(max_len):
        flag = 0
        cor_tree(i, 0)
        if flag == 0:
            answer += 1
    return answer




print(solution([[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]], [[1,2],[-1,-1],[-1,-1]]))
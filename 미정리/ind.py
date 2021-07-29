import sys
sys.stdin = open("ind.txt")
# Enter your code here. Read input from STDIN. Print output to STDOUT

num_sim_user = int(input())
num_reco_item = int(input())

num_users = int(input())
num_items = int(input())
num_rows = int(input())
MAP = [[0] * num_items for _ in range(num_users)]
reco_MAP = [[[0, __] for __ in range(num_users)] for _ in range(num_users)]
# print(reco_MAP)
for i in range(num_rows):
    p1, p2, scr = map(str, input().split())
    p1, p2, scr = int(p1), int(p2), float(scr)
    MAP[p1-1][p2-1] = scr
# [print(MAP[_]) for _ in range(num_users)]

for i in range(num_users):
    for j in range(i+1, num_users):
        vala, valb, valc, cnt = 0, 0, 0, 0
        for k in range(num_items):
            if MAP[i][k] and MAP[j][k]:
                vala += MAP[i][k] * MAP[j][k]
                valb += MAP[i][k] ** 2
                valc += MAP[j][k] ** 2
                cnt += 1
            elif MAP[i][k]:
                valb += MAP[i][k] ** 2
            elif MAP[j][k]:
                valc += MAP[j][k] ** 2
        if vala and cnt>1:
            res = round(vala / ((valb ** 0.5) * (valc ** 0.5)), 3)
            reco_MAP[i][j][0], reco_MAP[j][i][0] = res, res
# [print(reco_MAP[_]) for _ in range(num_users)]

num_reco_user = int(input())
users = []
for i in range(num_reco_user):
    users.append(int(input())-1)

user_weight = [0]*num_users
for i in range(num_users):
    weight, score = 0, 0
    for j in range(num_items):
        if MAP[i][j]:
            weight += MAP[i][j]
            score += 1
    user_weight[i] = weight/score
for i in users:
    reco_MAP[i].sort(reverse=True)
    resup = [[0, _] for _ in range(num_items)]
    resdown = [[0, _] for _ in range(num_items)]
    res = [[0, _] for _ in range(num_items)]
    for j in range(num_sim_user):
        if reco_MAP[i][j][0]:
            for k in range(num_items):
                now_comp = reco_MAP[i][j][1]
                if MAP[now_comp][k]:
                    resup[k][0] += user_weight[i]+reco_MAP[i][j][0]*(MAP[now_comp][k]-user_weight[now_comp])
                    resdown[k][0] += 1
    for j in range(num_items):
        if resdown[j][0]:
            res[j][0] = resup[j][0]/resdown[j][0]
    res.sort(reverse=True)
    res_num = num_reco_item
    for k in range(num_items):
        if not res_num:
            break
        if not MAP[i][res[k][1]]:
            print(res[k][1]+1, end=' ')
            res_num -= 1
    print()


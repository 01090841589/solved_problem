from bisect import bisect
def solution(info, query):
    answer = []
    db = [[] for _ in range(24)]

    for inf in info:
        orders = inf.split(" ")
        db_c = 0
        if orders[0][0] == 'j':
            db_c += 8
        elif orders[0][0] == 'p':
            db_c += 16
        if orders[1][0] == 'f':
            db_c += 4
        if orders[2][0] == 's':
            db_c += 2
        if orders[3][0] == 'p':
            db_c += 1
        db[db_c].append(int(orders[4]))
    for _ in range(24):
        db[_].sort()


    for qu in query:
        val = [1] * 24
        orders = qu.split(" ")
        if orders[0][0] == 'c':
            for i in range(8, 24):
                val[i] = 0
        elif orders[0][0] == 'j':
            for i in range(0, 8):
                val[i] = 0
            for i in range(16, 24):
                val[i] = 0
        elif orders[0][0] == 'p':
            for i in range(0, 16):
                val[i] = 0

        if orders[2][0] == 'f':
            for i in range(0, 4):
                val[i] = 0
            for i in range(8, 12):
                val[i] = 0
            for i in range(16, 20):
                val[i] = 0
        elif orders[2][0] == 'b':
            for i in range(4, 8):
                val[i] = 0
            for i in range(12, 16):
                val[i] = 0
            for i in range(20, 24):
                val[i] = 0

        if orders[4][0] == 's':
            for i in range(0, 24, 4):
                val[i] = 0
            for i in range(1, 24, 4):
                val[i] = 0
        elif orders[4][0] == 'j':
            for i in range(2, 24, 4):
                val[i] = 0
            for i in range(3, 24, 4):
                val[i] = 0
        if orders[6][0] == 'p':
            for i in range(0, 24, 2):
                val[i] = 0
        elif orders[6][0] == 'c':
            for i in range(1, 24, 2):
                val[i] = 0
        cnt = 0
        for i in range(24):
            if val[i] and db[i]:
                index = bisect(db[i], int(orders[7])-1)
                cnt += len(db[i]) - index
        answer.append(cnt)
    return answer

print(
solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])
)
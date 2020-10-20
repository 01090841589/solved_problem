def solution(record):
    answer = []
    order = []
    data = dict()
    for comm in record:
        co = comm.split(" ")

        if co[0][0] == "E":
            order.append([co[1], 1])
            data[co[1]] = co[2]
        elif co[0][0] == "L":
            order.append([co[1], 2])
        else:
            data[co[1]] = co[2]
    for pnt in order:
        if pnt[1] == 1:
            msg = data[pnt[0]] + "님이 들어왔습니다."
            answer.append(msg)
        else:
            msg = data[pnt[0]] + "님이 나갔습니다."
            answer.append(msg)
    return answer
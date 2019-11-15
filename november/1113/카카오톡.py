def solution(record):
    users = []
    com = []
    for i in range(len(record)):
        if record[i][0] == "E":
            user = ''
            for j in range(6, len(record[i])):
                if record[i][j] == ' ':
                    user_id = record[i][j+1:]
                    break
                user += record[i][j]
            users.append(user)
            for j in range(len(com)):
                if com[j][0] == user:
                    com[j][1] = user_id
            com.append([user, user_id, 0])
        elif record[i][0] == "L":
            user = ''
            for j in range(6, len(record[i])):
                if record[i][j] == ' ':
                    break
                user += record[i][j]
            users.remove(user)
            com.append([user, user_id, 1])
        elif record[i][0] == "C":
            user = ''
            for j in range(7, len(record[i])):
                if record[i][j] == ' ':
                    user_id = record[i][j+1:]
                    break
                user += record[i][j]
            for j in range(len(com)):
                if com[j][0] == user:
                    com[j][1] = user_id
    answer = []
    for i in range(len(com)):
        if com[i][2] == 0:
            answer.append(com[i][1] +"님이 들어왔습니다.")
        elif com[i][2] == 1:
            answer.append(com[i][1] +"님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
print(solution(["Enter uid1234 Muzi", "Leave uid1234", "Enter uid1234 Muzi", "Change uid1234 MMMM", "Leave uid1234", "Enter uid1234 Muzi", "Leave uid1234", "Enter uid1234 Muzi", "Leave uid1234", "Enter uid1234 Muzi", "Leave uid1234", "Enter uid1234 Muzi", "Leave uid1234", "Enter uid1234 Muzi2", "Leave uid1234", "Enter uid1234 Muzi2", "Change uid1234 MMMMM"]))
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo323","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan222","Leave uid1234","Enter uid14 Muzi","Change uid14 Ryan1","Enter uid1233 Muzi"]))
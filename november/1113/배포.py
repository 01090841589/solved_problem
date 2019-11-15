def solution(progresses, speeds):
    date = [0] * len(progresses)
    for i in range(len(progresses)):
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            date[i] += 1
    now = 0
    see = 0
    answer = []
    print(date)
    while date:
        if now < date[0]:
            if now != 0:
                answer.append(see+1)
            now = date.pop(0)
            see = 0

        else:
            date.pop(0)
            see += 1
    answer.append(see+1)
    return answer




print(solution([93,30,55], [1,30,5]))
print(solution([93,30,55,9], [1,30,5,2]))
def solution(n, words):
    answer = []
    use_word = []
    player = 0
    turn = 1
    flag = 1
    for word in words:
        if use_word == []:
            use_word.append(word)
            player += 1
            continue
        if use_word[-1][-1] == word[0]:
            if word not in use_word:
                use_word.append(word)
            else:
                flag = 0
                answer = [player+1,turn]
                break
        else:
            flag = 0
            answer = [player+1,turn]
            break
        player += 1
        if player == n:
            player = 0
            turn += 1

    if flag:
        answer = [0,0]

    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))



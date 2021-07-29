def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    second = ''
    third = ''
    # 2단계
    for chrr in new_id:
        chrr_asc = ord(chrr)
        if 97 <= chrr_asc <= 122 or 48 <= chrr_asc <= 57 or chrr_asc == 45 or chrr_asc == 95 or chrr_asc == 46:
            second += chrr
    # 3단계
    answer_size = len(second)
    for i in range(len(second)):
        if ord(second[i]) == 46:
            if i+1 < answer_size:
                if ord(second[i+1]) == 46:
                    continue
                else:
                    third += second[i]
            else:
                third += second[i]
        else:
            third += second[i]
    # 4단계
    fourth = third.strip(".")
    # 5단계
    if fourth:
        fifth = fourth
    else: fifth = "a"
    # 6단계
    if len(fifth) > 15:
        sixth = fifth[:15]
        sixth = sixth.strip(".")
    else: sixth = fifth
    # 7단계
    if len(sixth) < 3:
        answer = sixth + (3 - len(sixth)) * sixth[-1]
    else: answer = sixth
    return answer


# print(ord('a')) 97
# print(ord('z')) 122
# print(ord('0')) 48
# print(ord('9')) 57
# print(ord('-')) 45
# print(ord('_')) 95
# print(ord('.')) 46




solution("=.=")
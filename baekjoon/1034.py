def solution(s):
    answer = ""
    cs = 0

    while cs < len(s):
        if "0" <= s[cs] <= "9":
            answer += s[cs]
            cs += 1
        else:
            if s[cs] == "z":
                answer += "0"
                cs += 4
            elif s[cs] == "o":
                answer += "1"
                cs += 3
            elif s[cs] == "e":
                answer += "8"
                cs += 5
            elif s[cs] == "n":
                answer += "9"
                cs += 4
            elif s[cs] == "f":
                if s[cs+3] == 'r':
                    answer += "4"
                    cs += 4
                elif s[cs+3] == 'e':
                    answer += "5"
                    cs += 4
            elif s[cs] == "s":
                if s[cs+2] == 'x':
                    answer += "6"
                    cs += 3
                else:
                    answer += "7"
                    cs += 5
            elif s[cs] == "t":
                if s[cs+2] == 'o':
                    answer += "2"
                    cs += 3
                else:
                    answer += "3"
                    cs += 5



    return int(answer)



print(solution("2three45sixseven"))
print(solution("one4eight"))
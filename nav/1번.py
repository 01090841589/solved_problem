
def solution(record):
    answer = []
    buf = []
    for i in record:
        if i[0] == 'R':
            buf.append(i[8:])
        elif i[0] == 'D':
            if buf:
                buf.pop()
        elif i[0] == 'S':
            if buf:
                answer.extend(buf)
                buf = []
    return answer
print(solution(["RECEIVE abcd@naver.com", "RECEIVE zzkn@naver.com", "DELETE", "RECEIVE qwerty@naver.com", "SAVE", "RECEIVE QwerTY@naver.com"]))
print(solution(["RECEIVE abcd@naver.com", "RECEIVE zzkn@naver.com", "DELETE", "RECEIVE qwerty@naver.com", "SAVE", "RECEIVE QwerTY@naver.com", "SAVE"]))
print(solution(["RECEIVE abcd@naver.com", "RECEIVE zzkn@naver.com", "DELETE", "RECEIVE qwerty@naver.com", "SAVE", "RECEIVE QwerTY@naver.com"]))

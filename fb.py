# answer = 0
# def solution(k):
#     global answer
#     def matches(t, scr, site):
#         global answer
#         if t == 0:
#             answer += scr
#             return
#         if site == 0:
#             if t == 6:
#                 answer += 1
#             for i in first:
#                 if t >= i[0]:
#                     matches(t-i[0], scr*i[1], site+1)
#                 else:
#                     return
#         else:
#             for i in other:
#                 if t >= i[0]:
#                     matches(t-i[0], scr*i[1], site+1)
#                 else:
#                     return
#     first = [[2, 1], [3, 1], [4, 1], [5, 3], [6, 2], [7, 1]]
#     other = [[2, 1], [3, 1], [4, 1], [5, 3], [6, 3], [7, 1]]
#     matches(k, 1, 0)
#
#     return answer
#
# print(solution(11))


def solution(num):
    global answer
    answer = 0
    ran = [0, 0, 1, 1, 1, 3, 3, 1]
    nums = [0, 0, 1]
    answer = 0
    for i in range(3, num + 1):
        res = 0
        for minus in range(2, 8):

            if i == minus:
                if i == 6:
                    res += 2
                    continue
                res += ran[minus]
            elif i > minus:
                res += nums[i - minus] * ran[minus]
            else:
                break
        nums.append(res)
    answer = nums[num]
    return answer


print(solution(1))
print(solution(2))

print(solution(3))

print(solution(4))

print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))
print(solution(11))
print(solution(50))
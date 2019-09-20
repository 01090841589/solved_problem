# import sys
# sys.stdin = open("숫자만들기.txt")
#
# def calcul(cnt, k):
#     if k == N-1-sums:
#         print(operation)
#         # cals()
#     for i in range(k, N-1):
#         # if operation[k] == operation[i]:
#         #     continue
#         operation[k], operation[i] = operation[i], operation[k]
#         calcul(cnt, k+1)
#         operation[k], operation[i] = operation[i], operation[k]
#
#
#
# def cals():
#     global MAX, MIN
#     res = nums[0]
#     for i in range(N-1):
#         if operation[i] == '+':
#             res = res + nums[i+1]
#         elif operation[i] == '-':
#             res = res - nums[i + 1]
#         elif operation[i] == '*':
#             res = res * nums[i + 1]
#         elif operation[i] == '/':
#             res = int(res / nums[i+1])
#     if MAX < res:
#         MAX = res
#     if MIN > res:
#         MIN = res
#     print(res)
# opera = ['+', '-', '*', '/']
# T = int(input())
# for tc in range(1, 2):
#     N = int(input())
#     op = list(map(int, input().split()))
#     nums = list(map(int, input().split()))
#     operation = []
#     sums = 0
#     for i in range(4):
#         if op[i] > 1:
#             sums += op[i]-1
#     for a in range(4):
#         operation.extend([opera[a]] * op[a])
#     MAX = -100000000
#     MIN = 100000000
#     visited = [0] * (N-1)
#     calcul(nums[0], 0)
#
#     # print('#{} {}'.format(tc, MAX-MIN))
a = [1, 2]
a.remove(3)
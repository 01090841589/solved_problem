# import sys
# sys.stdin = open("소수완제품.txt")
#
# def succ(k, per, scr, now):
#     global result
#     if k == 18:
#         if scr in not_prime:
#             result += now
#         return
#     succ(k+1, per, scr+1, now*per)
#     succ(k+1, per, scr, now*(1-per))
#
# T = int(input())
# for tc in range(1, T+1):
#     A, B = map(int, input().split())
#     not_prime = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
#     result = 0
#     succ(0, A*0.01, 0, 1)
#     a_per = result
#     result = 0
#     succ(0, B*0.01, 0, 1)
#     b_per = result
#     print('#%s %.6f' %(tc, 1-(a_per*b_per)))

a = 'ababa'
print(a.count('aba'))
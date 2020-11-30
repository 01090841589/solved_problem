import sys
sys.stdin = open("19392.txt")
from collections import deque
from collections import deque

prod = list(map(int, input().split()))
orders = input()

minus, start = 1, 0
nums = []
oper = []
operation = ['+', '-', '*', '/']
buf = ''


def calculate(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2
    if oper == '/':
        if num1 * num2 >= 0:
            return num1 // num2
        else:
            if abs(num1 % num2):
                return (num1 // num2) + 1
            else:
                return (num1 // num2)


for i in range(len(orders)):
    if '0' <= orders[i] <= '9':
        buf += orders[i]
    else:
        nums.append(int(buf))
        oper.append(orders[i])
        buf = ''

nums.append(int(buf))
input_oper = ['', '', '', '']
for i, pr in enumerate(prod):
    input_oper[pr - 1] = operation[i]
for i in range(3, -1, -1):
    print(nums)
    now = input_oper[i]
    for i in range(len(oper) - 1, -1, -1):
        if oper[i] == now:
            res = calculate(nums[i + 1], nums[i], oper[i])
            del oper[i]
            nums[i] = res
            del nums[i + 1]

if len(oper):
    res = calculate(nums[1], nums[0], oper[0])
else:
    res = nums[0]

print(res)
import sys
sys.stdin = open("1938.txt")
from collections import deque

orders = input()
minus, start = 1, 0
nums = deque()
oper = deque()
operation = ['+', '*', '-', '/']
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


if orders[0] == '-':
    minus = -1
    start = 1
for i in range(start, len(orders)):
    if '0' <= orders[i] <= '9':
        buf += orders[i]
    else:
        nums.append(int(buf))
        oper.append(orders[i])
        buf = ''
nums.append(int(buf))
nums[0] *= minus
while len(oper) > 1:
    left = (operation.index(oper[0])) % 2
    right = (operation.index(oper[-1])) % 2
    if left > right:
        num = calculate(nums.popleft(), nums.popleft(), oper.popleft())
        nums.appendleft(num)
    elif left < right:
        num = calculate(nums[-2], nums[-1], oper.pop())
        nums.pop()
        nums.pop()
        nums.append(num)
    else:
        left_cal = calculate(nums[0], nums[1], oper[0])
        right_cal = calculate(nums[-2], nums[-1], oper[-1])
        if left_cal >= right_cal:
            nums.popleft()
            nums.popleft()
            nums.appendleft(left_cal)
            oper.popleft()
        else:
            nums.pop()
            nums.pop()
            nums.append(right_cal)
            oper.pop()
    print(nums, oper)
if len(oper):
    res = calculate(nums[0], nums[1], oper[0])
else:
    res = nums[0]
print(res)
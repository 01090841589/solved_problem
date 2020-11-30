import sys
sys.stdin = open("19392.txt")
from collections import deque
first = list(map(int, input().split()))
sik = list(input())


prod = first[:]
orders = sik[:]

def calcul(num1,num2,op):
    if op =='+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    else:
        if num1*num2 >= 0:
            return num1//num2
        else:
            if num1%num2 :
                return num1//num2 +1
            else:
                return num1//num2

sik2 = []
tem = ''
for i in sik:
    if '0' <= i and i<='9':
        tem += i
    else:
        sik2.append(int(tem))
        sik2.append(i)
        tem = ''
sik2.append(int(tem))

cal = []
opers = []

def check(a):
    if a =='+':
        return first[0]
    elif a == '-':
        return first[1]
    elif a == '*':
        return first[2]
    elif a == '/':
        return first[3]
for i in range(len(sik2)-1,-1,-1):
    if type(sik2[i]) == int:
        cal.append(sik2[i])
    else:
        if opers:
            now = check(sik2[i])
            while opers and now <= check(opers[-1]):
                cal.append(opers.pop())
            opers.append(sik2[i])
        else:
            opers.append(sik2[i])
while opers:
    cal.append(opers.pop())
stack = []
for a in cal:
    if type(a) == int:
        stack.append(a)
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(calcul(num1, num2, a))

print(stack[0])
print(stack[0])




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
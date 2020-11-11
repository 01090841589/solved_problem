import sys
sys.stdin = open("1938.txt")

sik = list(input())

def det_oper(a,su,su2):
    if a == '+':
        return su+su2
    elif a == '-':
        return su-su2
    elif a == '*':
        return su*su2
    else:
        if (su >0 and su2 <0) or (su <0 and su2 > 0):
            if su%su2:
                return su//su2+1
            else: return su//su2
        else:
            return su//su2

if sik[0] == '-':
    f = 1
    m = -1
else: f = 0; m = 1

numbers = []
opers = []
tem = ''
for i in range(f,len(sik)):
    if sik[i] in '1234567890':
        tem += sik[i]
    else:
        if len(numbers) == 0:
            numbers.append(m*int(tem))
        else:
            numbers.append(int(tem))
        tem = ''
        opers.append(sik[i])
numbers.append(int(tem))

front, back = 0, len(numbers)-1
f,b = 0, len(opers)-1
flag = True

num1, num2 = numbers[front], numbers[back]

if len(opers) == 0:
    ans = num1
else:
    while flag :
        oper1, oper2 = opers[f], opers[b]

        if f == b:
            ans = det_oper(oper1,num1,num2)
            flag = False
        else:
            if oper1 in '*/' and oper2 in '+-':
                tem = numbers[front+1]
                num1 = det_oper(oper1,num1,tem)
                front +=1
                f +=1
            elif oper1 in '+-' and oper2 in '*/':
                tem = numbers[back-1]
                num2 = det_oper(oper1,tem,num2)
                back -=1
                b -=1
            else:
                tem = numbers[front+1]
                tem2 = numbers[back-1]
                tem_num1 = det_oper(oper1,num1,tem)
                tem_num2 = det_oper(oper2,tem2,num2)
                if tem_num1 >= tem_num2:
                    num1 = tem_num1
                    front +=1
                    f += 1
                else:
                    num2 = tem_num2
                    back -= 1
                    b -= 1

print(ans)
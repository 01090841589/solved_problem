import sys
sys.stdin = open("ddd.txt")
digit = ['0', '1', '2', '3' ,'4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
password = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
NUMS = input()
result_0b = ''
for a in NUMS:
    num = ''
    k = digit.index(a)
    while k > 0:
        if k % 2:
            num += '1'
        else:
            num += '0'
        k //= 2
    while len(num) < 4:
        num += '0'
    for i in range(3, -1, -1):
        result_0b += num[i]
i = 0
while i < len(result_0b)-5:
    if result_0b[i:i+6] in password:
        print(password.index(result_0b[i:i+6]), end = ', ')
        i += 6
        continue
    i += 1
    lst = ['', '1', '101']
    for k in range(len(lst)):
        lst[k] = '0'*(4-len(lst[k]))+lst[k]
    print(lst)
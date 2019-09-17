import sys
sys.stdin = open("dd.txt")
digit = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

NUMS = list(input())
print(NUMS)
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
for i in range(len(result_0b)//7+1):
    deco = result_0b[i * 7:(i + 1) * 7]
    if deco == '':
        break
    digit_10 = 0
    for a, b in enumerate(deco):
        digit_10 += int(b) * 2 ** (len(deco)-a-1)
    print(digit_10, end = ' ')

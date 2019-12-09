import sys
sys.stdin = open("이진수.txt")

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
T = int(input())
for tc in range(1, T+1):
    N, num = map(str, input().split())
    result = ''
    for i in num:
        n = nums.index(i)
        bina = []
        while n:
            if n % 2:
                bina.insert(0, '1')
            else:
                bina.insert(0, '0')
            n //= 2
        while len(bina) < 4:
            bina.insert(0, '0')
        result += ''.join(bina)
    print('#{} {}'.format(tc, result))
import sys
sys.stdin = open("계산기.txt")


def make_num(k):
    if k != '' and int(k) > X:
        return
    elif k != '':
        calcul.append(int(k))
    for a in nums:
        make_num(k+str(a))


T = int(input())
for tc in range(1, 3):
    result = 999999
    num = list(map(int, input().split()))
    nums = []
    for i in range(10):
        if num[i]:
            nums.append(i)
    calcul = []
    X = int(input())
    make_num('')
    calcul.sort()
    print(calcul)
    if result == 999999:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, result))
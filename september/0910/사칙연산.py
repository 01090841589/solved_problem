import sys
sys.stdin = open("사칙연산.txt")
def calcul(k):
    if len(node[k]) == 4:
        return str(eval(calcul(int(node[k][2]))+node[k][1]+calcul(int(node[k][3]))))
    else:
        return node[k][1]
for tc in range(1, 11):
    N = int(input())
    node = [list(input().split()) for i in range(N)]
    node.insert(0, [])
    print('#{} {}'.format(tc, round(float(calcul(1)))))

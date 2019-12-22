import sys
sys.stdin = open("고속도로건설.txt")

def UF(num):
    if num == node[num]:
        return num
    return UF(node[num])



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())
    rodes = []
    node = [i for i in range(N+1)]
    for i in range(M):
        rodes.append(list(map(int, input().split())))
    rodes.sort(key=lambda k: k[2])
    buf = 0
    res = 0
    for rode in rodes:
        if buf == N-1:
            break
        left = UF(rode[0])
        right = UF(rode[1])
        if left == right:
            continue
        node[right] = node[left]
        res += rode[2]
        buf += 1
    print('#{} {}'.format(tc, res))
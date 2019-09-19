import sys
sys.stdin = open("베이비진게임.txt")

def babygin(M, k):
    if len(M) < 3:
        return
    for i in range(len(M)-2):
        if M[i] == M[i+1] == M[i+2] or M[i]+1 == M[i+1] == M[i+2]-1 :
            result[k] = 1
            return



T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    result = [0, 0]
    for i in range(12):
        if i % 2:
            p2.append(cards[i])
            p2.sort()
            babygin(p2, 1)
        else:
            p1.append(cards[i])
            p1.sort()
            babygin(p1, 0)
    if result[0] == result[1]:
        print('#{} 0'.format(tc))
    elif result[0]:
        print('#{} 1'.format(tc, result))
    elif result[1]:
        print('#{} 2'.format(tc, result))
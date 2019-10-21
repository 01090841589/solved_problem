import sys
sys.stdin = open("2번.txt")

def goyut(n, cnt):
    if player[n][1] == 0:
        player[n][0] += cnt*20
        if player[n][0] == 100:
            player[n][1] = 1
        if player[n][0] == 200:
            player[n][1] = 2
        if player[n][0] > 400:
            player[n][0] = 500
    elif player[n][1] == 1:
        a = MAP1.index(player[n][0])
        a += cnt
        if a > 6:
            player[n][0] = 300+20*(a-6)
            player[n][1] = 0
        else:
            player[n][0] = MAP1[a]
        if player[n][0] == 250:
            player[n][1] = 2
    elif player[n][1] == 2:
        a = MAP2.index(player[n][0])
        a += cnt
        if a > 6:
            player[n][0] = 500
        else:
            player[n][0] = MAP2[a]


def yut(k):
    global result
    if k == 10:
        if result < player[0][0]+player[1][0]+player[2][0]+player[3][0]:
            result = player[0][0]+player[1][0]+player[2][0]+player[3][0]
        return
    if player[0][0] == 0:
        oriscr = player[0][0]
        orik = player[0][1]
        goyut(0, node[k])
        yut(k+1)
        player[0][0] = oriscr
        player[0][1] = orik

    elif player[1][0] == 0:
        if player[0][0] < 500:
            oriscr = player[0][0]
            orik = player[0][1]
            goyut(0, node[k])
            yut(k+1)
            player[0][0] = oriscr
            player[0][1] = orik

        oriscr = player[1][0]
        orik = player[1][1]
        goyut(1, node[k])
        if player[0][0] != player[1][0]:
            yut(k+1)
        elif player[0][0] == 500:
            yut(k+1)
        player[1][0] = oriscr
        player[1][1] = orik

    elif player[2][0] == 0:
        if player[0][0] < 500:
            oriscr = player[0][0]
            orik = player[0][1]
            goyut(0, node[k])
            if player[0][0] != player[1][0] and player[0][0] != player[2][0]:
                yut(k+1)
            elif player[0][0] == 500:
                yut(k+1)
            player[0][0] = oriscr
            player[0][1] = orik

        if player[1][0] < 500:
            oriscr = player[1][0]
            orik = player[1][1]
            goyut(1, node[k])
            if player[1][0] != player[2][0] and player[1][0] != player[0][0]:
                yut(k+1)
            elif player[1][0] == 500:
                yut(k+1)
            player[1][0] = oriscr
            player[1][1] = orik

        if player[2][0] < 500:
            oriscr = player[2][0]
            orik = player[2][1]
            goyut(2, node[k])
            if player[2][0] != player[0][0] and player[2][0] != player[1][0]:
                yut(k+1)
            elif player[2][0] == 500:
                yut(k+1)
            player[2][0] = oriscr
            player[2][1] = orik

    else:
        if player[0][0] < 500:
            oriscr = player[0][0]
            orik = player[0][1]
            goyut(0, node[k])
            if player[0][0] != player[1][0] and player[0][0] != player[2][0] and player[0][0] != player[3][0]:
                yut(k+1)
            elif player[0][0] == 500:
                yut(k+1)
            player[0][0] = oriscr
            player[0][1] = orik

        if player[1][0] < 500:
            oriscr = player[1][0]
            orik = player[1][1]
            goyut(1, node[k])
            if player[1][0] != player[0][0] and player[1][0] != player[2][0] and player[1][0] != player[3][0]:
                yut(k+1)
            elif player[1][0] == 500:
                yut(k+1)
            player[1][0] = oriscr
            player[1][1] = orik

        if player[2][0] < 500:
            oriscr = player[2][0]
            orik = player[2][1]
            goyut(2, node[k])
            if player[2][0] != player[0][0] and player[2][0] != player[1][0] and player[2][0] != player[3][0]:
                yut(k+1)
            elif player[2][0] == 500:
                yut(k+1)
            player[2][0] = oriscr
            player[2][1] = orik

        if player[3][0] < 500:
            oriscr = player[3][0]
            orik = player[3][1]
            goyut(3, node[k])
            if player[3][0] != player[0][0] and player[3][0] != player[1][0] and player[3][0] != player[2][0]:
                yut(k+1)
            elif player[3][0] == 500:
                yut(k+1)
            player[3][0] = oriscr
            player[3][1] = orik



T = int(input())
for tc in range(1, T+1):
    node = list(map(int,input().split()))
    player = [[0, 0, 0] for _ in range(4)]
    MAP1 = [100, 150, 200, 250, 270, 290, 300]
    MAP2 = [200, 210, 230, 250, 300, 350, 400]
    result = 0
    yut(0)
    print('#{} {}'.format(tc, result))
import sys
sys.stdin = open("2번.txt")

def goyut(n, cnt):
    if player[n][1] == 0:
        player[n][0] += cnt*2
        if player[n][0] == 10:
            player[n][1] = 1
        if player[n][0] == 20:
            player[n][1] = 2
        if player[n][0] >= 40:
            player[n][0] = 40
    elif player[n][1] == 1:
        a = MAP1.index(player[n][0])
        a += cnt
        if a > 7:
            # player[n][0] = 30+2*(a-8)
            player[n][0] = 40
            player[n][1] = 0
        else:
            player[n][0] = MAP1[a]
        # if player[n][0] == 25:
        #     player[n][1] = 2
    elif player[n][1] == 2:
        a = MAP2.index(player[n][0])
        a += cnt
        if a > 6:
            player[n][0] = 40
        else:
            player[n][0] = MAP2[a]


def yut(k, scr):
    global result, final
    if k == 10:
        if result < scr:
            result = scr
        return
    if player[0][0] == 0:
        oriscr = player[0][0]
        orik = player[0][1]
        goyut(0, node[k])
        yut(k+1, scr+player[0][0])
        player[0][0] = oriscr
        player[0][1] = orik

    elif player[1][0] == 0:
        if player[0][0] < 40:
            oriscr = player[0][0]
            orik = player[0][1]
            goyut(0, node[k])
            yut(k+1, scr+player[0][0])
            player[0][0] = oriscr
            player[0][1] = orik

        oriscr = player[1][0]
        orik = player[1][1]
        goyut(1, node[k])
        if player[0][0] != player[1][0]:
            yut(k+1, scr+player[1][0])
        elif player[0][0] == 40:
            yut(k+1, scr+player[1][0])
        player[1][0] = oriscr
        player[1][1] = orik

    elif player[2][0] == 0:
        if player[0][0] < 40:
            oriscr = player[0][0]
            orik = player[0][1]
            goyut(0, node[k])
            if player[0][0] != player[1][0] and player[0][0] != player[2][0]:
                yut(k+1, scr+player[0][0])
            elif player[0][0] == 40:
                yut(k+1, scr+player[0][0])
            player[0][0] = oriscr
            player[0][1] = orik

        if player[1][0] < 40:
            oriscr = player[1][0]
            orik = player[1][1]
            goyut(1, node[k])
            if player[1][0] != player[2][0] and player[1][0] != player[0][0]:
                yut(k+1, scr+player[1][0])
            elif player[1][0] == 40:
                yut(k+1, scr+player[1][0])
            player[1][0] = oriscr
            player[1][1] = orik

        if player[2][0] < 40:
            oriscr = player[2][0]
            orik = player[2][1]
            goyut(2, node[k])
            if player[2][0] != player[0][0] and player[2][0] != player[1][0]:
                yut(k+1, scr+player[2][0])
            elif player[2][0] == 40:
                yut(k+1, scr+player[2][0])
            player[2][0] = oriscr
            player[2][1] = orik

    else:
        if player[0][0] < 40:
            oriscr = player[0][0]
            orik = player[0][1]
            goyut(0, node[k])
            if player[0][0] != player[1][0] and player[0][0] != player[2][0] and player[0][0] != player[3][0]:
                yut(k+1, scr+player[0][0])
            elif player[0][0] == 40:
                yut(k+1, scr+player[0][0])
            player[0][0] = oriscr
            player[0][1] = orik

        if player[1][0] < 40:
            oriscr = player[1][0]
            orik = player[1][1]
            goyut(1, node[k])
            if player[1][0] != player[0][0] and player[1][0] != player[2][0] and player[1][0] != player[3][0]:
                yut(k+1, scr+player[1][0])
            elif player[1][0] == 40:
                yut(k+1, scr+player[1][0])
            player[1][0] = oriscr
            player[1][1] = orik

        if player[2][0] < 40:
            oriscr = player[2][0]
            orik = player[2][1]
            goyut(2, node[k])
            if player[2][0] != player[0][0] and player[2][0] != player[1][0] and player[2][0] != player[3][0]:
                yut(k+1, scr+player[2][0])
            elif player[2][0] == 40:
                yut(k+1, scr+player[2][0])
            player[2][0] = oriscr
            player[2][1] = orik

        if player[3][0] < 40:
            oriscr = player[3][0]
            orik = player[3][1]
            goyut(3, node[k])
            if player[3][0] != player[0][0] and player[3][0] != player[1][0] and player[3][0] != player[2][0]:
                yut(k+1, scr+player[3][0])
            elif player[3][0] == 40:
                yut(k+1, scr+player[3][0])
            player[3][0] = oriscr
            player[3][1] = orik



node = list(map(int,input().split()))
player = [[0, 0, 0] for _ in range(4)]
MAP1 = [10, 13, 16, 19, 25, 30, 35, 40]
MAP2 = [20, 22, 24, 25, 30, 35, 40]
result = 0
yut(0,0)
print(result)
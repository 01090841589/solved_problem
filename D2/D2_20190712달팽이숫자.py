

def snail_num(A) :
    snail=[]
    for i in range(A):
        a = []
        for j in range(A):
            a.append(0)
        snail.append(a)
    # 행렬 생성

    snail[0][0] = 1
    #첫 값 생성

    for i in range(1,A):
        snail[0][i] = snail[0][i-1]+1
    # 첫 줄 완성
    a = A-1
    b = 0
    x = A-1
    y = 0
    for i in range(A-1,0,-2):
        if (A-i) % 2 == 1  :
            for b in range(i) :
                snail[y+1][x] = snail[y][x]+1
                y = y+1
            for b in range(i) :
                snail[y][x-1] = snail[y][x]+1
                x = x-1
            if i > 1 :
                for b in range(i-1) :
                    snail[y-1][x] = snail[y][x]+1
                    y = y-1
                for b in range(i-1) :
                    snail[y][x+1] = snail[y][x]+1
                    x = x + 1
    # for i in range(1,A-1)
    # for i in range(1,A):
    for a in range(A):
        for b in range(A):
            print(snail[a][b],end=' ')
        print('')

T = int(input())
for i in range(T):
    A = int(input())
    print('#{0}'.format(i+1))
    snail_num(A)
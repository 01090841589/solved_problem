T = 1
N = 6
M = 5
line = ['WWWWWWWWWWWWWW','WWRRWWBBBBBBWW','WRRRWWWBWWWWRB','WWBWBWWWBWRRRR','WBWBBWWWBBWRRW', 'WWWBWWWWWWWWWW']
W = []
B = []
R = []
for i in range(N):
    # color = input()
    # line.append(color)
    W.append(line[i].count('W'))
    B.append(line[i].count('B'))
    R.append(line[i].count('R'))
print(W,B,R)
total= [0,0,0,0,0,0]
total[0] = len(line[0])-line[0].count('W')
total[len(line)-1] = len(line[len(line)-1])-line[len(line)-1].count('R')
for White in range(len(line)-3,-1,-1): #3 2 1 0
    for count_White in range(1,White+1): # 123 12 1 -
        print('W')
        total[count_White] = len(line[count_White])-line[count_White].count('W')
    for Red in range(len(line)-White-2): # 0 01 012 0123
        print('B') #len(line)-White 로 역순
        for count_Blue in range(len(line)-2,len(line)-3-Red,-1): # 4 34 234 1234
            total[count_Blue] = len(line[count_Blue]) - line[count_Blue].count('B')
        print(total,sum(total))
        if White < len(line)-3: # - -,4 -,4,43 -,4,43,432
            for count_Red in range(len(line)-2,len(line)) : #
                total[count_Red] = len(line[count_Red]) - line[count_Red].count('R')
        # for count_Red in range(0,len(line)-White-2): # 0 01 012 0123
        #     total[White+count_Blue+1] = len(line[White+count_Blue+1])-line[White+count_Blue+1].count('B')
    print(total,sum(total))



'''
for문이용, w값 내려가면서 나머지 RB경우의수 비교
'''
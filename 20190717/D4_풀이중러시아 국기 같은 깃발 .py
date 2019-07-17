T = 1
N = 4
M = 5
line = ['WWWWWWWWWWWWWW','WWRRWWBBBBBBWW','WRRRWWWBWWWWRB','WWBWBWWWBWRRRR','WBWBBWWWBBWRRW', 'WWWWWWWWWWWWWW']
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
        total[count_White] = len(line[count_White])-line[count_White].count('W')
    for Red in range(len(line)-White-2): # 0 01 012 0123
        for count_Blue in range(0,len(line)-White-2): # 0 01 012 0123
            total[White+count_Blue+1] = len(line[White+count_Blue+1])-line[White+count_Blue+1].count('B')
        print(total,sum(total))



'''
for문이용, w값 내려가면서 나머지 RB경우의수 비교
'''
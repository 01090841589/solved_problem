import math
TEST = int(input())
GRADE = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
def calcul(K,N):
    score = []
    grade = []
    student = 0
    for i in range(K):
        score.append(input().split(' '))
        grade.append(int(score[i][0])*0.35+int(score[i][1])*0.45+int(score[i][2])*0.20)
    student = grade[N-1]
    SCORE = sorted(grade,reverse=True)
    for i in range(K):
        if student == SCORE[i]:
            return(GRADE[int((i)/K*10)])
for k in range(TEST):
    inp = input().split(' ')
    K = int(inp[0])
    N = int(inp[1])
    print('#{0} {1}'.format(k+1, calcul(K, N)))
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score


    def name(self):
        return self.name

    def score(self):
        return self.score

    def __repr__(self):
        return self.name
    def scr(self):
        result = self.score
        return result
score1 = input().split(', ')
s1 = Student("국어", int(score1[0]))
s2 = Student("영어", int(score1[1]))
s3 = Student("수학", int(score1[2]))
print('국어, 영어, 수학의 총점: {0}'.format(s1.scr()+s2.scr()+s3.scr()))
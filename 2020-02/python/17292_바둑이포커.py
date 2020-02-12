import sys
sys.stdin = open("바둑이포커.txt")

cards = list(input().split(','))
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
print(cards)
first_grade = []
second_grade = []
third_grade = []
for i in range(6):
    for j in range(i+1, 6):
            print(cards[i], cards[j])
            if abs(number.index(cards[i][0]) - number.index(cards[j][0])) == 1 or abs(number.index(cards[i][0]) - number.index(cards[j][0])) == 14:
                print('first')
                first_grade.append([cards[i], cards[j]])
            elif cards[i][1] == cards[j][1]:
                print('second')
                second_grade.append([cards[i], cards[j]])
            else:
                print('third')
                third_grade.append([cards[i], cards[j]])

print(first_grade, second_grade, third_grade)
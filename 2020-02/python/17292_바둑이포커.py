import sys
sys.stdin = open("바둑이포커.txt")


def countscore(card1, card2):
    scr = 0
    if card1[1] == card2[1]:
        scr += 100000
    scr += (max(number.index(card1[0]) , number.index(card2[0])))*1000
    scr += (min(number.index(card1[0]) , number.index(card2[0])))*10
    if number.index(card1[0]) > number.index(card2[0]):
        if card1[1] == 'b':
            scr += 1
    else:
        if card2[1] == 'b':
            scr += 1
    return scr

cards = list(input().split(','))
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
result = []
for i in range(6):
    for j in range(i+1, 6):
        score = countscore(cards[i], cards[j])
        if abs(number.index(cards[i][0]) - number.index(cards[j][0])) == 1 or abs(number.index(cards[i][0]) - number.index(cards[j][0])) == 14:
            result.append([cards[i], cards[j], score+3000000])
        elif cards[i][0] == cards[j][0]:
            score = countscore(cards[i], cards[j])
            result.append([cards[i], cards[j], score+2000000])
        else:
            score = countscore(cards[i], cards[j])
            result.append([cards[i], cards[j], score+1000000])
result.sort(key=lambda k:k[2], reverse=True)
for i in range(15):
    print('{}{}'.format(result[i][0], result[i][1]))
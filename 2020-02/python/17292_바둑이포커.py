import sys
sys.stdin = open("바둑이포커.txt")

cards = list(input().split(','))

print(cards)
for i in range(6):
    for j in range(i, 6):
        if i != j:

            print(cards[i], cards[j])
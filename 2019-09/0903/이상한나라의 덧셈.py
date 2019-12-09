import sys
sys.stdin = open('이상한.txt')

T = int(input())
for tc in range(1, T+1):
    game = list(map(int, input()))
    a = 0
    while len(game) > 1:
        c = game.pop()+game.pop()
        if c > 9:
            game.append(1)
            game.append(c%10)
        else:
            game.append(c)
        a += 1
    if a % 2:
        print('#{} A'.format(tc))
    else:
        print('#{} B'.format(tc))

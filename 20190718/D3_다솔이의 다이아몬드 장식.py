T = int(input())
for test_case in range(T):
    word = input()
    deco = ['.','.','#','.','.']
    for i in range(len(word)):
        deco[0] += '.#..'
        deco[1] += '#.#.'
        deco[2] += '.{0}.#'.format(word[i])
        deco[3] += '#.#.'
        deco[4] += '.#..'
    for i in range(len(deco)):
        print(deco[i])
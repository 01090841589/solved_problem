def bin_6(num) :
    bin = [0,0,0,0,0,0]
    if num >= 32 :
        bin[0] = 1
        num -= 32
    if num >= 16 :
        bin[1] = 1
        num -= 16
    if num >= 8 :
        bin[2] = 1
        num -= 8
    if num >= 4 :
        bin[3] = 1
        num -= 4
    if num >= 2 :
        bin[4] = 1
        num -= 2
    if num == 1 :
        bin[5] = 1
    return bin
def encoder(spell) :
    if 65<= ord(spell) <=90 :
        str_int = ord(spell) - 65
    elif 97 <= ord(spell) <= 122 :
        str_int = ord(spell) - 97 + 26
    elif 48 <= ord(spell) <= 57 :
        str_int = ord(spell) + 4
    elif ord(spell) == 43 :
        str_int = ord(spell) + 19
    elif ord(spell) == 47 :
        str_int = ord(spell) + 16
    return bin_6(str_int)

T = int(input())
for test_case in range(1,T+1) :
    deco = ''
    dec_str = ''
    string = input()
    for str_dec in range(len(string)) :
        bin_num = encoder(string[str_dec])
        for i in range(6):
            deco += str(bin_num[i])
    print('#{0} '.format(test_case),end='')
    while len(deco) > 0 :
        print(chr(int('0b'+deco[0:8],2)),end='')
        deco = deco.replace(deco[0:8],'',1)
    print('')
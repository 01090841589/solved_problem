'''
print(ord('A'))65
print(ord('Z'))90
print(ord('a'))97
print(ord('z'))122
print(ord('0'))48
print(ord('9'))57
print(ord('+'))43
print(ord('/'))47
'''
def bin_6(num) :
    bin = [0,0,0,0,0,0]
    if num > 32 :
        bin[0] = 1
        num /= 2
    if num > 16 :
        bin[1] = 1
        num -= 16
    if num > 8 :
        bin[2] = 1
        num -= 8
    if num > 4 :
        bin[3] = 1
        num -= 4
    if num > 2 :
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


deco = ''
string = 'TGlmZSBpdHNlbGYgaXMgYSBxdW90YXRpb24u'
for str_dec in range(len(string)) :
    print(encoder(string[str_dec]))
# print(deco)
# print(int(deco[0:6]))
# print(chr(32+1+2+4))
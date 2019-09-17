import sys
sys.stdin = open("암호코드스캔.txt")
dec_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
dec_bina = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
password_map = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

T = int(input())
for tc in range(1,4):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]
    # [print(MAP[i]) for i in range(N)]
    codes = []
    total = 0



    for a in range(N):
        code = ''
        front, back = 0, M
        flag = 1
        cnt = 0
        for b in range(M):
            if MAP[a][b] != '0':
                if flag:
                    flag = 0
                    front = b
                cnt = 0
            else:
                cnt += 1









    for CODE in codes:
        print(CODE)
        decode = ''
        CODE = '0000' + CODE
        for right in CODE:
            decode += dec_bina[dec_num.index(right)]
        while decode[-1] == '0':
            decode = '0' + decode[:-1]
        if len(decode) > 336:
            continue
        if 280 < len(decode) < 336:
            while len(decode) > 280:
                decode = decode[1:]
        if len(decode) == 280:
            short = ''
            for i in range(len(decode)//5):
                short += decode[i*5]
            decode = short
        if 224 < len(decode) < 280:
            while len(decode) > 224:
                decode = decode[1:]
        if len(decode) == 224:
            short = ''
            for i in range(len(decode)//4):
                short += decode[i*4]
            decode = short
        if 168 < len(decode) < 224:
            while len(decode) > 168:
                decode = decode[1:]
        if len(decode) == 168:
            short = ''
            for i in range(len(decode)//3):
                short += decode[i*3]
            decode = short
        if 112 < len(decode) < 168:
            while len(decode) > 112:
                decode = decode[1:]
        if len(decode) == 112:
            short = ''
            for i in range(len(decode)//2):
                short += decode[i*2]
            decode = short
        if 56 < len(decode) < 112:
            while len(decode) > 56:
                decode = decode[1:]


        if len(decode) == 56:
            password = []
            flag = 1
            for i in range(8):
                try:
                    dec = decode[i*7:(i+1)*7]
                    password.append(password_map.index(dec))
                except:
                    flag = 0
                    break
            # print(password)
            if flag and (((password[0]+password[2]+password[4]+password[6])*3) + (password[1]+password[3]+password[5])) % 10 == (10-password[7])%10:
                total += sum(password)
    print('#{} {}'.format(tc, total))
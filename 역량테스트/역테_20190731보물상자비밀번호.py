T = int(input())
for test_case in range(1, T+1):
    NK = list(map(int,input().split()))
    n = list(map(str,input()))
    password = [['' for _ in range(NK[0]//4)] for _ in range(4)]
    for i,j  in enumerate(n):
        n[i] = int('0x'+n[i],16)
    i = 0
    for compo in range(4):
        for rot in range(NK[0]//4):
            password[compo][rot] = n[i]
            i += 1
    total_war = []
    mov_N = []
    for cascad in range((NK[0]//4)):
        for wor in password:
            total = 0
            for a,num in enumerate(wor):
                total += num*16**(NK[0]//4-1-a)
            total_war.append(total)
            mov_N.append(wor.pop())
        for i,wor in enumerate(mov_N):
            password[(i+1)%4].insert(0,wor)
        mov_N = []
    total_war = list(set(total_war))
    total_war.sort(reverse=True)
    print('#{0} {1}'.format(test_case,total_war[NK[1]-1]))
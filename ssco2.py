import sys
sys.stdin = open("ssco2.txt")


S = int(input())

ans = []
R = int(S ** 0.5)
scr = 0
for i in range(1, S, 2):
    scr += i
    if scr <= S:
        ans.append(i)
    else:
        scr -= i
        scr = S - scr
        if scr % 2:
            A = ans.pop()
            ans[-1] += (scr+A)
        else:
            ans[-1] += scr
        break
print(ans)
print(len(ans))
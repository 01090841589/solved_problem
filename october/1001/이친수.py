N = int(input())
num = []
for i in range(N):
    if i < 2:
        num.append(1)
    else:
        num.append(num[-1]+num[-2])
print(num[-1])
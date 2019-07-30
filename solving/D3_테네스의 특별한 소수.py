import math
def prime(num):
    for i in range(3, int(math.sqrt(num))+1):
        if num % i == 0:
           return False
    return True

sosu = [2]
for a in range(3,1000000, 2):
    if prime(a):
        sosu.append(a)
for num in sosu:
    print(num,end=' ')

def prime(num):
    for i in range(2, num):
        if num % i == 0:
           return False
    return True

sosu = []

for a in range(2,100000):
    if prime(a):
        sosu.append(a)
print(sosu)

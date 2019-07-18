def squrt_num(num):
    for i in range(1,21):
        if i**2 > num:
            break
    min = i-1
    max = i
    for i in range(1,21):
        if ((max+min)/2)**2 > num :
            max = (max+min)/2
        else :
            min = (max+min)/2
    return min,max
print(squrt_num(int(input())))
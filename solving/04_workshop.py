def squrt_num(num):
    for i in range(1,21):
        if i**2 > num:
            break
    min = i-1
    max = i
    while (abs(((max+min)/2)**2-num) > 0.0000001):
        if ((max+min)/2)**2 > num :
            max = (max+min)/2
        else :
            min = (max+min)/2
    return min,max
print(squrt_num(int(input())))
def rec_power(x, n):
    if n == 1: return x
    if n % 2 == 0:
        y = rec_power(x, n//2)
        return y*y
    else:
        y = rec_powre(x, (n-1)//2)
        return  y*y*n
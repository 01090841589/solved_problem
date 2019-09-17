def summ(n, scr):
    if n == 0:
        print(scr)
        return
    summ(n-1, scr+n)

summ(100, 0)
def perm(n, r, q):
    if r == 0:
        cont
    else:
        for i in range(n-1, -1, -1):
            a[i], a[i-1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            perm(n-1, r-1, q)
            a[i], a[i-1] = a[n-1], a[i]

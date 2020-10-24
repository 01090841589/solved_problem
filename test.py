
def isPrime(n):
    m = int((n+1) ** 0.5)
    for i in range(2, m + 1):
        if prime[i]:
            for j in range(i+i, n+1, i):
                prime[j] = 0
    if prime[n]:
        return 1
    else:
        intt = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                intt.append(i)
                if i != n//i:
                    intt.append(n//i)
        intt.sort()
        return intt[1]
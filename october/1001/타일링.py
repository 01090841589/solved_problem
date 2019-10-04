
m = [1, 1, 3]
N = int(input())
for i in range(3, N+1):
    m.append((m[i-1] + 2*m[i-2])%10007)
print(m[N])

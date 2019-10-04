N = int(input())
num = list(map(int, input().split()))
num.sort()
result = 0
for i in range(N):
    result += num[i]*(N-i)
print(result)
import sys
sys.stdin = open("거스름돈.txt")

def money(scr, k):
    global result
    if k >= result:
        return
    if scr < 0:
        return
    if scr == 0:
        if result > k:
            result = k
        return
    for i in range(n):
        money(scr-amount[i], k+1)



m = int(input())
n = int(input())
amount = list(map(int, input().split()))
result = 999999
amount.sort(reverse=True)

money(m, 0)
print(result)
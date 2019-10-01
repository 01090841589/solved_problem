def find_num(k):
    global result
    if k > N:
        return
    if k == N:
        result += 1
    find_num(k+1)
    find_num(k+2)
    find_num(k+3)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = 0
    find_num(0)
    print(result)
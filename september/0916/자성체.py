import sys
sys.stdin = open("자성체.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mag = list(map(int, input().split()))
    # for i in range(1, N):
    #     left =
    #     right =
    d = (mag[0]+mag[1])/N
    while (mag[2] / ((mag[0] - d) * (mag[0] - d)) - mag[3] / ((mag[1] - d) * (mag[1] - d))) > 0.000001:
        try:
            print(mag[2] / ((mag[0] - d) * (mag[0] - d)) - mag[3] / ((mag[1] - d) * (mag[1] - d)))
            if (mag[2] / ((mag[0] - d) * (mag[0] - d)) - mag[3] / ((mag[1] - d) * (mag[1] - d))) > 0:
                d += d/2
                print(d)
        except:
            print('error')
            continue
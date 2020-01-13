import sys
sys.stdin = open("스노우볼.txt")


H, x = map(int, input().split())
balls = []
for i in range(H):
    balls.append(int(input()))
result = 0
for i in range(H-1, -1, -1):
    snowball = balls[i]
    result += snowball
    result *= x
print(result%1000000007)
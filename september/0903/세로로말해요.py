import sys
sys.stdin = open('세로로.txt')

for tc in range(1,int(input())+1):
    inp = [input() for _ in range(5)]
    result = [inp[j][i] for i in range(15) for j in range(5) if i < len(inp[j])]
    print('#{} {}'.format(tc, ''.join(result)))
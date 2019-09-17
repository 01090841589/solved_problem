import sys
sys.stdin = open('색종이.txt')


def find_paper():
    for y in range(10):
        for x in range(10):
            for i in range(5, 0, -1):
                if statch_paper(y, x, i):
                    paper_delete(y, x, i)
                    [print(MAP[i]) for i in range(10)]
                    print()
                    z

def statch_paper(y, x, n):
    for i in range(n):
        for j in range(n):
            if x+n-1 < 10 and y+n-1 < 10:
                if MAP[y+i][x+j] == 1:
                    continue
                else:
                    return
            else:
                return
    return True


def paper_delete(y, x, n):
    if paper[n-1] > 0:
        paper[n-1] -= 1
        for i in range(n):
            for j in range(n):
                MAP[y+i][x+j] = 0


def paper_restore(y, x, n):
    for i in range(n):
        for j in range(n):
            MAP[y + i][x + j] = 1


T = int(input())
for tc in range(1, T+1):
    MAP = [list(map(int, input().split())) for _ in range(10)]
    paper = [5] * 5
    papers = []
    total = 0
    find_paper()
    for i in range(5):
        total += 5 - paper[i]
        if paper[i] < 0:
            total = -1
            break
    print('#{} {}'.format(tc, total))
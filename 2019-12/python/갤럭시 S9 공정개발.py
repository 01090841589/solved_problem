import sys
sys.stdin = open("파일합치기.txt")

from itertools import accumulate
def filesum(size, files) -> int:
    answer = [[0 for _ in range(size + 1)] for __ in range(size + 1)]
    knuth = [[col if row == col - 1 else 0 for col in range(size + 1)] for row in range(size + 1)]
    accum_sum, current = list(accumulate(files)), 0
    for step in range(2, size + 1):
        for row in range(0, size - step + 1):
            col = row + step
            sum_in_range = accum_sum[col] - accum_sum[row]
            answer[row][col] = INF
            for div in range(knuth[row][col - 1], knuth[row + 1][col] + 1):
                left, right = answer[row][div], answer[div][col]
                if answer[row][col] > left + right + sum_in_range:
                    answer[row][col] = left + right + sum_in_range
                    knuth[row][col] = div
    return answer[0][size]


tc = int(input())
for _ in range(tc):
    k, files = int(input()), list(map(int, input().split()))
    INF = k*10000
    if k == 1:
        ans = 0
    else:
        files.insert(0, 0)
        ans = filesum(k, files)

    print('#{} {}'.format(_+1, ans))

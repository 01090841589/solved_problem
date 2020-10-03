answer = 0
def solution(histogram):
    global answer
    def bin_ser(start, end, l, r, prev):
        if start > end:
            return
        global answer
        mid = (start + end) // 2
        left, right = -1, -1
        for i in range(leng):
            if histogram[i] >= mid:
                left = i
                break
        for i in range(leng-1, left, -1):
            if histogram[i] >= mid:
                right = i
                break
        if answer < (right-left-1) * mid:
            answer = (right-left-1) * mid

        if right == -1:
            bin_ser(start, mid-1, left, right, mid)
        else:
            if left == l and right == r and prev > mid:
                bin_ser(mid+1, end, left, right, mid)
            else:
                bin_ser(mid+1, end, left, right, mid)
                bin_ser(start, mid-1, left, right, mid)

    answer = 0
    leng = len(histogram)

    start = 0
    end = max(histogram)
    bin_ser(start, end, 0, leng-1, 0)

    return answer


print(solution([2, 2, 2, 3]))
print(solution([6, 5, 7, 3, 4, 2]))
print(solution(range(10000)))

# answer = 0
# leng = len(histogram)
# max_leng = max(histogram)
#
# for i in range(leng // 2):
#     if answer < min(histogram[i], histogram[leng // 2 + i]) * (leng // 2 - 1):
#         answer = min(histogram[i], histogram[leng // 2 + i]) * (leng // 2 - 1)
#
# for i in range(leng - 1, 1, -1):
#     if max_leng * (i - 1) <= answer:
#         break
#     for j in range(leng - i):
#         scr = min(histogram[j], histogram[j + i]) * (i - 1)
#         if answer < scr:
#             answer = scr
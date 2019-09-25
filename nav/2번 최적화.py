
def solution(n):
    answer = 0
    nums = set()
    nums.add(2)
    N = (n+2)
    for i in range(2, N):
        buf = 1
        cnt = 0
        for j in range(i, 1, -1):
            if i < j //2:
                break
            if j > 1:
                buf *= j
                if buf > 10 ** 12 + 1:
                    break
                cnt += 1
                if cnt > 1:
                    nums.add(buf)
    nums = list(nums)
    nums.sort()
    answer = nums[n-1]
    return answer

print(solution(1))
print(solution(2))
print(solution(4))
print(solution(9))
print(solution(30))
print(solution(50))
print(solution(70))
print(solution(100))
print(solution(300))
print(solution(500))
print(solution(700))
print(solution(1000))
print(solution(3000))
print(solution(5000))
print(solution(7000))
print(solution(10000))
print(solution(30000))
print(solution(50000))
print(solution(70000))
print(solution(100000))
print(solution(300000))
print(solution(500000))
print(solution(700000))
print(solution(1000000))
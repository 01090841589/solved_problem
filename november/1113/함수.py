def solution(n):
    answer = ''
    nums = [0,0,0,0,0,0,0,0,0,0]
    while n > 0:
        nums[n % 10] += 1
        n //= 10
    for i in range(9, -1, -1):
        while nums[i] > 0:
            answer += str(i)
            nums[i] -= 1
    answer = int(answer)
    return answer




print(solution(128372))
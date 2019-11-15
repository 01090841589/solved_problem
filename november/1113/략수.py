def solution(n):
    answer = 0
    for i in range(n, 0, -1):
        if i == n**0.5:
            answer += i
        if i < n**0.5:
            break
        for j in range(i-1, 0, -1):
            if i*j == n:
                answer += i+j
    return answer


print(solution(5))
print(solution(2))
print(solution(4))
print(solution(3000))
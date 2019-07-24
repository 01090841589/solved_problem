def check(month, result):
    global min_value
    print(result)
    if month >= 12:
        if result < min_value:
            min_value = result
    else:
        check(month + 1, result + cost[0] * months[month])
        check(month + 1, result + cost[1])
        check(month + 3, result + cost[2])


for tc in range(1, int(input()) + 1):
    cost = list(map(int, input().split()))
    months = list(map(int, input().split()))

    min_value = cost[3]
    check(0, 0)
    print(cost,months)
    print(f"#{tc} {min_value}")
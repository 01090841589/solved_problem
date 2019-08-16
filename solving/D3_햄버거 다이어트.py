# T = 1
# N = 5
# L = 1000
# score = [[200,100],[500,300],[300,250],[1000,500],[400,400]]
# score.sort(reverse = True)
# print(score)
# for i in range(len(score)):
#     cal = score[i][1]
#     for j in range(1,len(score)):
#         cal
#
# total = 0
def main():
    num_tests = 1
    for test in range(1, num_tests + 1):
        numbers, limits = (5, 1000)
        profits = [[0 for _ in range(limits + 1)] for _ in range(numbers + 1)]
        print(profits)
        values = []
        calories = []
        for _ in range(numbers):
            value, calorie = tuple(map(int, input().strip().split()))
            values.append(value)
            calories.append(calorie)

        max_profit = 0
        for n in range(1, numbers + 1):
            for l in range(limits + 1):
                if calories[n - 1] <= l:
                    profits[n][l] = max(profits[n - 1][l], values[n - 1] + profits[n - 1][l - calories[n - 1]])
                else:
                    profits[n][l] = profits[n - 1][l]

                if profits[n][l] > max_profit:
                    max_profit = profits[n][l]

        print('#%d %d' % (test, max_profit))


if __name__ == "__main__":
    main()
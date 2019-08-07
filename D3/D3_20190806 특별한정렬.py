T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    numbers = list(map(int,input().split()))
    num_sort = []
    for i in range(len(numbers)//2):
        num_sort.append(max(numbers))
        numbers.remove(max(numbers))
        num_sort.append(min(numbers))
        numbers.remove(min(numbers))
    if numbers != []:
        num_sort.append(numbers[0])
    print('#{}'.format(test_case,num_sort), end = ' ')
    for i in range(10):
        print(num_sort[i],end = ' ')
    print()
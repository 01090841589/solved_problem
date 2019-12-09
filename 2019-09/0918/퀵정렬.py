import sys
sys.stdin = open("퀵정렬.txt")

def QuickSort(input_list):
    if len(input_list) < 2:
        return input_list

    pivot = input_list[0]
    less = [i for i in input_list[1:] if i <= pivot]
    greater = [i for i in input_list[1:] if i > pivot]

    input_list = QuickSort(less) + [pivot] + QuickSort(greater)

    return input_list

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = QuickSort(arr)
    print('#{} {}'.format(tc, arr[N//2]))
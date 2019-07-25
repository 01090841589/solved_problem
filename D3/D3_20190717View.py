for test_case in range(1,11):
    count = int(input())
    building = input().split(' ')
    building = [x for x in building if x]
    building = list(map(int,building))
    max_view = 0
    for i in range(2, len(building)-2):
        view = building[i]
        if building[i] - building[i + 1] < view:
            if building[i] - building[i + 1] > 0 :
                view = building[i] - building[i + 1]
            else :
                view = 0
        if building[i] - building[i + 2] < view:
            if building[i] - building[i + 2] > 0 :
                view = building[i] - building[i + 2]
            else :
                view = 0
        if building[i] - building[i - 1] < view:
            if building[i] - building[i - 1] > 0 :
                view = building[i] - building[i - 1]
            else :
                view = 0
        if building[i] - building[i - 2] < view:
            if building[i] - building[i - 2] > 0 :
                view = building[i] - building[i - 2]
            else :
                view = 0
        max_view += view
    print('#{0} {1}'.format(test_case,max_view))
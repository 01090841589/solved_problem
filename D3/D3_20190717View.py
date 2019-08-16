# import sys
# sys.stdin = open("view_input.txt")
def views(a):
    global view
    global i
    if building[i] - building[i + a] < view:
        if building[i] - building[i + a] > 0:
            view = building[i] - building[i + a]
        else:
            view = 0
for test_case in range(1,11):
    count = int(input())
    building = list(map(int, input().split()))
    max_view = 0
    for i in range(2, len(building)-2):
        view = building[i]
        views(-2)
        views(-1)
        views(1)
        views(2)
        max_view += view
    print('#{0} {1}'.format(test_case,max_view))
from itertools import permutations

def find(nums):
    global flag
    if flag == 1:
        return
    n = len(nums)
    if n == 1:
        if nums[0] == 2:
            flag = 1
        return
    a = []
    b = []
    for i in range(1, n-1):
        b.append(nums[i - 1])
        b.append(nums[i])
        b.append(nums[i + 1])
        b.remove(max(b))
        b.remove(min(b))
        a.append(b.pop())
    find(a)

    return
result = [0,0,0,0,0,0,0,0,0]
flag = 0
# for a in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15):
#     if flag:
#         print(a)
#         break
#     find(list(a))
# print('1')
for a in permutations([14, 12, 10, 8, 6, 4, 1, 2, 3, 5, 7, 9, 11, 13, 15], 15):
    if flag:
        print(a)
        break
    find(list(a))
print('1')

a = [0]
b = [0,0,0]
c = []



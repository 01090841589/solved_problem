import sys
sys.stdin = open("스들.txt")


def cal_num(k):
    if sum(doors) == 1:
        for i in range(3):
            if doors[i]:
                door_num[i] = k
    else:
        right = []
        for i in range(3):
            if doors[i]:
                right.append(door_alp[i])
        i = 0
        while right:
            if door_num[door_alp.index(right[i])] != -1:
                k -= door_num[door_alp.index(right[i])]
                right.pop(i)
            else:
                i += 1
            if i == len(right):
                break
        if right:
            door_num[door_alp.index(''.join(right))] = k


N = int(input())
for tc in range(1, 5):
    p, q = map(int, input().split())
    words = [input() for _ in range(p)]
    mine = [input() for _ in range(q)]
    # [print(words[_]) for _ in range(p)]
    doors = [0, 0, 0]
    door_alp = ['a', 'b', 'c', 'ab', 'ac', 'ac', 'abc']
    door_num = [-1, -1, -1, -1, -1, -1, -1]
    for i in range(p):
        cnt = 0
        flag = 1
        for j in words[i]:
            if j == '.' and flag:
               cnt += 1
            elif flag:
                cal_num(cnt)
                flag = 0
                if j == '(':
                    doors[0] += 1
                elif j == '{':
                    doors[1] += 1
                elif j == '[':
                    doors[2] += 1
                elif j == ')':
                    doors[0] -= 1
                elif j == '}':
                    doors[1] -= 1
                elif j == ']':
                    doors[2] -= 1
            else:
                if j == '(':
                    doors[0] += 1
                elif j == '{':
                    doors[1] += 1
                elif j == '[':
                    doors[2] += 1
                elif j == ')':
                    doors[0] -= 1
                elif j == '}':
                    doors[1] -= 1
                elif j == ']':
                    doors[2] -= 1
        # print(doors, cnt)
        if sum(doors) == 0:
            cnt = 0
        # print(doors, cnt)
    print(door_num)
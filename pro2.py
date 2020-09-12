from itertools import combinations


def solution(orders, course):
    menu = set()
    custo = len(orders)
    custo_num = [0] * custo
    select = [[0] * 26 for _ in range(custo)]
    completed_menu = [1] * 20
    for i in course:
        completed_menu[i] = 0

    for numbers in range(custo, 1, -1):
        vali = range(custo)
        sub_menu = set()
        buf = []
        for members in combinations(vali, numbers):
            res = 0
            for mem in members:
                if res == 0:
                    res = set(orders[mem])
                else:
                    res = res & set(orders[mem])

            if len(res) > 1:
                res = list(res)
                res.sort()
                sel_menu = ''
                for i in res:
                    sel_menu += i
                if completed_menu[len(sel_menu)] == 0:

                    sub_menu.add(sel_menu)
                for k in range(len(sel_menu), 1, -1):
                    if completed_menu[k] == 0:
                        for adds in combinations(sel_menu, k):
                            add_menus = ''
                            for j in adds:
                                add_menus += j

                            menu.add(add_menus)
                            buf.append(k)

        for add_menu in sub_menu:
            completed_menu[len(add_menu)] = 1
            menu.add(add_menu)
            for k in range(len(add_menu), 1, -1):
                if completed_menu[k] == 0:
                    for adds in combinations(add_menu, k):
                        add_menus = ''
                        for j in adds:
                            add_menus += j
                        menu.add(add_menus)
                    completed_menu[k] = 1

    answer = list(menu)
    answer.sort()
    return answer


print(solution(["AB", "ABC", "ABCD", "ABCDE", "ABCDEF","AB", "ABC", "ABCD", "ABCDE", "ABCDEF"], [2, 3, 4, 5, 6]))
# print(solution(["XYZ", "XWY", "WXA", "YZA", "XYA", "WXY"], [2,3,4]))
# print(solution(["AB", "BC", "CD", "DE", "EF", "ABCDEF", "ABC"], [2, 3]))
# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH","ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH","ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4, 5, 6]))
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))


# print(ord("A"))
#
# A = set('ABCD')
# B = set('BCF')
# print(A & B)
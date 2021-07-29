from collections import deque, defaultdict

def solution(customer, K):
    answer = []
    in_cus = []
    out_cus = []
    all_out = defaultdict(int)
    for cus in customer:
        if cus[1]:
            in_cus.append(cus[0])
            all_out[cus[0]] += 1
        else:
            out_cus.append(cus[0])
            all_out[cus[0]] -= 1

    # 결과적으로 나간사람들 정리
    new_ins = []
    new_ous = []
    for ins in in_cus:
        if all_out[ins]:
            new_ins.append(ins)
    for ous in out_cus:
        if all_out[ous]:
            new_ous.append(ous)
    in_use = [1] * len(new_ins)

    start = 0
    for num in new_ous:
        now = -1
        for i in range(start, len(new_ins)):

            if in_use[i]:
                if now == -1:
                    now = i
                if new_ins[i] == num:
                    in_use[i] = 0
                    break
        if start < now:
            start = now
    ans_num = 0
    for i in range(len(new_ins)):
        if ans_num == K:
            break
        if in_use[i]:
            answer.append(new_ins[i])
            ans_num += 1
    answer.sort()
    return answer


def solution(price):
    answer = [-1] * len(price)

    price_box = [[price[0], 0]]

    for i in range(1, len(price)):
        while True:
            if price_box and price_box[-1][0] < price[i]:
                pri, ind = price_box.pop()
                answer[ind] = i-ind
            else:
                break
        price_box.append([price[i], i])



    return answer


from collections import defaultdict

def solution(orders):
    answer = []
    answer_num = 0
    foods = defaultdict(dict)
    for order in orders:
        all_orders = list(order.split(" "))
        if not foods[all_orders[0]]:
            foods[all_orders[0]] = defaultdict(int)
        for ord in range(1, len(all_orders)):
            foods[all_orders[0]][all_orders[ord]] += 1
    for customer in foods.keys():
        if answer_num < len(foods[customer]):
            answer_num = len(foods[customer])
            answer= [customer]
        elif answer_num == len(foods[customer]):
            answer.append(customer)
    answer.sort()
    return answer


def solution(strs):
    answer = ""
    min_str = 1000
    for i in strs:
        if len(i) < min_str:
            min_str = len(i)
    flag = 0
    for i in range(min_str):
        comp = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != comp:
                flag = 1
                break
        else:
            answer += comp
        if flag:
            break

    return answer
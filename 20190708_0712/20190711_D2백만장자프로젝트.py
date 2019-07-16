def cal_max_price(price) :
    total = 0
    stock = 0
    max_price = 0
    for i in range(B) :
        for j in range(i,B) :
            if price[i] < price[j]:
                total += price[i]
                stock += 1
                break
        Z = 0
        for k in range(i+1,B) :
            if price[i] > price[k] :
                Z += 1
            else :
                break
            if Z == B-i-1 :
                for l in range(stock) :
                    max_price += price[i]
                    stock -= 1
    for l in range(stock) :
        max_price += price[i]
        stock -= 1
    return (max_price - total)

A = int(input())
for a in range(A) :
    B = int(input())
    price = []
    input_price = []
    input_price.append(input().split(' '))
    for i in range(B) :
        price.append(int(input_price[0][i]))
    C = cal_max_price(price)
    print('#{0} {1}'.format(a+1, C))
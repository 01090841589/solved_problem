def transnum(num,trans):
    total = 0
    a = 1
    for i in range(len(num)-1,-1,-1):
        total += num[i]*a
        a *= trans
    return total
T = int(input())
for test_cate in range(1,T+1):
    total = []
    n = input()
    m = input()
    N = list(map(int, n))
    M = list(map(int, m))
    n_numbers = []
    m_numbers = []
    for i in range(0, len(N)):
        error_N = N[:]
        if error_N[i] % 2 :
            error_N[i] = 0
        else:
            error_N[i] = 1
        n_numbers.append(transnum(error_N,2))

    for i in range(0, len(M)):
        m_list = []
        error_M = M[:]
        if error_M[i] % 3 == 0:
            error_M[i] = 1
            m_list.append(transnum(error_M, 3))
            error_M[i] = 2
            m_list.append(transnum(error_M, 3))
        elif error_M[i] == 1:
            error_M[i] = 0
            m_list.append(transnum(error_M, 3))
            error_M[i] = 2
            m_list.append(transnum(error_M, 3))
        else:
            error_M[i] = 0
            m_list.append(transnum(error_M, 3))
            error_M[i] = 1
            m_list.append(transnum(error_M, 3))
        m_numbers.append(m_list)
    for A in n_numbers:
        for B in m_numbers:
            for C in B:
                if A == C:
                    total.append(A)
    print('#{0} {1}'.format(test_cate,total[0]))
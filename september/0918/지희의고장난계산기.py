import sys
sys.stdin = open("계산기.txt")

# by Nine
'''
               ___                                    ___
              |   | 0-9                   1-9        |   |
     1-9      v   |                    ----------->  v   | 0-9
    ----->   state0   ----->  state1  <-----------   state2
                        *                    *
'''


def backtrack(k, goal, n0, n1, state):
    global MIN_D
    if MIN_D != -1 and k + 1 >= MIN_D: return

    # print(k,n0,n1,state)
    if state == 0:
        for i in range(10):
            if DigitBn[i]:
                val = n1 * 10 + i
                if val > goal: return
                if val == goal:
                    if MIN_D == -1 or MIN_D > k + 1: MIN_D = k + 1
                    return
                backtrack(k + 1, goal, n0, val, 0)  # 계속 state0
        if n1 not in visited or visited[n1] > k + 1: visited[n1] = k + 1; backtrack(k + 1, goal, n1, 0, 1)
    elif state == 1:
        for i in range(10):
            if DigitBn[i]:
                if i == 0: continue
                if n0 * i > goal: return
                if n0 * i == goal:
                    if MIN_D == -1 or MIN_D > k + 1: MIN_D = k + 1
                    return
                backtrack(k + 1, goal, n0, i, 2)
    elif state == 2:
        for i in range(10):
            if DigitBn[i]:
                val = n0 * (n1 * 10 + i)
                if val > goal: return
                if val == goal:
                    if MIN_D == -1 or MIN_D > k + 1: MIN_D = k + 1
                    return
                backtrack(k + 1, goal, n0, n1 * 10 + i, 2)  # 계속 state2
        if n1 != 1:
            if (n0 * n1) not in visited or visited[n0 * n1] > k + 1: visited[n0 * n1] = k + 1; backtrack(k + 1, goal, n0 * n1, 0, 1)
    return

TC = int(input())
for tc in range(1, TC + 1):
    DigitBn = list(map(int, input().split()))
    X_str = input()
    X = int(X_str)
    MIN_D = -1
    visited = {}
    for i in range(10):
        if DigitBn[i] == 0: continue
        if i == X:
            MIN_D = 1
            break
        if i == 0: continue
        backtrack(1, X, 1, i, 0)
    print("#%d %d" % (tc, -1 if MIN_D == -1 else MIN_D + 1))
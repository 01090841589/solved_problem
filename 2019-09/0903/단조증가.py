import sys
sys.stdin = open('단조증가.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = [-1]
    for i in range(N - 1):
        for j in range(i + 1, N):
            comp = str(nums[i]*nums[j])
            if len(comp) == 1:
                continue
            else:
                for a in range(len(comp) - 1):
                    if comp[a] <= comp[a+1]:
                        if a == (len(comp)-2):
                            result.append(nums[i]*nums[j])
                        continue
                    else:
                        break
    print('#{} {}'.format(tc, max(result)))


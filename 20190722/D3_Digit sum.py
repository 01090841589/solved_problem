T = int(input())
ans = []
for tc in range(T):
    n = int(input()) - 1
    ans.append(n % 9 + 1)

for t in range(len(ans)):
    print("#{} {}".format(t + 1, ans[t]))
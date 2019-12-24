import sys
sys.stdin = open("욕심쟁이판다.txt")

n = int(input())
li = []
for _ in range(n):
  li.append([int(x) for x in input().split()])
res = [min(li[0])]
print(res)
for i in range(1, n):
  tmp = []
  for j in li[i]:
    if res[i-1] < j:
      tmp.append(j)
  if tmp:
    tmp = min(tmp)
    res.append(tmp)
print(res)
print(len(res))
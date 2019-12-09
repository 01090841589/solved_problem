import sys
sys.stdin = open('test.txt')
n = int(input())
a = [input().split() for _ in range(n)]
data=[]
print(a)
for i in range(len(a)):
   if a[i][0] == 'push':
       data.append(int(a[i][1]))
   elif a[i][0] == 'top':
       if len(data) == 0:
           print(-1)
       else:
           print(data[-1])
   elif a[i][0] == 'pop':
       if len(data) == 0:
           print(-1)
       else:
           print(data.pop())
   elif a[i][0] == 'size':
       print(len(data))
   elif a[i][0] == 'empty':
       if len(data) == 0:
           print(1)
       else:
           print(0)
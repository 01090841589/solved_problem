import sys
sys.stdin = open("16472.txt")

from collections import defaultdict

N = int(input())
words = list(input())
left = right = 0
t=len(set(words))
n=len(words)
jewelry=defaultdict(int)
res=0
if t <= N:
    print(len(words))
else:
    while True:
        if len(jewelry) > N:
            jewelry[words[left]]-=1
            if jewelry[words[left]] == 0:
                del jewelry[words[left]]
            left+=1
        elif right == n:
            break
        else:
            jewelry[words[right]]+=1
            right+=1
        if len(jewelry) == N:
            if res < right-left:
                res = right-left
    print(res)
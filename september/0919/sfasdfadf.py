from collections import deque



A = deque()
A.append(1)
print(A)

B = list()
B.append(A.popleft())
print(A, B)
a = [1,2,3,4,5]
b = [10, 20, 30, 40, 50]
c = [100, 200, 300, 400, 500]
AA = [A+B+C for A in a for B in b for C in c]
print(AA)
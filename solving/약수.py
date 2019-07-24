n = 6
m = 2
measure = []
measure_mul = []
for i in range(1, n+1):
    if n%i == 0:
        measure.append(i)
measure_mul = measure[:]
for a in range(m-1):
    measure_times = measure_mul[:]
    for i in measure:
        for j in measure_times:
            measure_mul.append(i*j)
    measure_mul = list(set(measure_mul))
    measure_mul.sort()
print(sum(measure_mul)%1000000007)
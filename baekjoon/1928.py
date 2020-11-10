def dd(su, su2):
    if (su > 0 and su2 < 0) or (su < 0 and su2 > 0):
        if su % su2:
            return su // su2 + 1
        else:
            return su // su2
    else:
        return su // su2

print(dd(16, -3))
print(dd(-16, 3))
print(dd(16, 3))
print(dd(-16, -3))
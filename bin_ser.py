from bisect import bisect
a = 100
db = [99, 100, 100, 100]

l, r = 0, len(db)
# while True:
#     mid =(l+r) // 2
#     if a <= db[mid]:
index = bisect(db, a)

print(index)
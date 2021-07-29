# 문제
# student = {'python' : 80, 'algorithm' : 99, 'django' : 89, 'flask' : 83}
# avg = 0
# print(sum(student.values())/len(student))
# 문제
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
men = {'A' : 0, 'B' : 0, 'O' : 0, 'AB': 0}
for blood in blood_types :
    men[blood] += 1
for blo, men in men.items():
    print('{0}형 : {1}명'.format(blo,men))
# import keyword
# print(keyword.kwlist)
def positive_sum(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

print(positive_sum([1, -4, 7, 12]))


def calc(equation):

    cnt = 0
    total = 0
    for i, j in enumerate(equation):
        if j in ['+','-']:
            if i !=0:
                total += int(equation[cnt:i])
                cnt = i
    total += int(equation[cnt:])
    return total

print(calc('123+2-124'))
print(calc('-12+12-7979+9191'))
print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'point:({},{})'.format(self.x,self.y)


class Circle(Point):
    def __init__(self, center , r):
        self.r = r
        self.center = (center.x, center.y)
    def get_area(self):
        return self.r**2*3.14
    def get_perimeter(self):
        return 2*self.r*3.14
    def get_center(self):
        return (self.center)
    def __str__(self):
        return 'Circle:({0}),r:{1}'.format(self.center, self.r)


p1 = Point(0,0)
print(p1)
c1 = Circle(p1,3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
print(c1)
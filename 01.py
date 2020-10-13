import math

print('Длины сторон треугольника:')
b = float(input('b= '))
c = float(input('c= '))
print('Косинус угла между стороной b и c:')
cos_x = 10
while 1 < cos_x or -1 > cos_x:
    cos_x = float(input('cos(x'))
a = math.sqrt(math.pow(b, 2) + math.pow(c, 2) - (2 * b * c * cos(x)))
print(int(a))

import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.a_angle = round(
            (180 / math.pi) * (math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c))), 3)
        self.b_angle = round(
            (180 / math.pi) * (math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c))), 3)
        self.c_angle = round(
            (180 / math.pi) * (math.acos((self.b ** 2 + self.a ** 2 - self.c ** 2) / (2 * self.b * self.a))), 3)

    def is_triangle(self):
        return not (self.a + self.b < self.c or self.b + self.c < self.a or self.a + self.c < self.b)

    def area(self):
        return round(math.sqrt(
            self.half_perimeter() * (self.half_perimeter() - self.a) * (self.half_perimeter() - self.b) * (
                        self.half_perimeter() - self.c)), 2) if self.is_triangle() else 'Error'

    def half_perimeter(self):
        return (self.a + self.b + self.c) / 2 if self.is_triangle() else 'Error'

    def perimeter(self):
        return self.a + self.b + self.c if self.is_triangle() else 'Error'

    def __str__(self):
        return f'a - {self.a_angle}, b - {self.b_angle}, c - {self.c_angle}, ' if self.is_triangle() else 'Error'


class Isosceles_triangle(Triangle):
    def __init__(self, a, b):
        super().__init__(a=a, b=a, c=b)

class Equilateral_triangle(Triangle):
    def __init__(self, a):
        super().__init__(a=a, b=a, c=a)



class Rectangle:
    def __init__(self, a, b):  # c, d):
        self.angles = 4
        self.a = a
        self.b = b
        # self.c = c
        # self.d = d

    def area(self):
        # if self.a == self.c and self.b == self.d:
        #     return self.a * self.b
        # if (self.a == self.c and self.b != self.d) or (self.a != self.c and self.b == self.d):
        #     return "That's not a rectangle"
        return self.a * self.b

    def perimeter(self):
        return 2*self.a + 2*self.b  # + self.c + self.d

class Parallelogram(Rectangle):
    def __init__(self, a, b, h):            #       _____b______
        super().__init__(a=a, b=b)          #    a / |<h       /
        self.h = h                          #     /__|________/

    def area(self):
        return self.b*self.h

    def perimeter(self):
        return 2*self.a + 2*self.b
#                                                                      a
class Right_trapezia:                                          #      ____
    def __init__(self, a, b, c, d): # a//c ; /\bc = 90 and /\ab = 90: |   \
        self.a = a                                             #      |____\
        self.b = b                               #                      c^
        self.c = c
        self.d = d

    def area(self):
        return (self.c*self.b)-(0.5*self.b*(self.c-self.a))

    def perimeter(self):
        return self.a + self.b + self.c + self.d

class Trapezoid(Parallelogram):
    def __init__(self, a, b, c, d, h):
        super().__init__(a=a, b=b, h=h)
        self.c = c
        self.d = d

    def area(self):
        return (self.a + self.c / 2) * self.h

    def perimeter(self):
        return self.a + self.b + self.c + self.d


# triangle = Triangle(a=3, b=4, c=5)
# print(triangle)
# iso_tr = Isosceles_triangle(3, 4)
# print(iso_tr)
# eq_tr = Equilateral_triangle(1)
# print(eq_tr)

trapezoid = Right_trapezia(3, 4, 6, 5)
print(trapezoid.area())

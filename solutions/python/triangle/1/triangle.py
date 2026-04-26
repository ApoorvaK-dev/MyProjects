def triangle(a,b,c):
    return a>0 and b>0 and c>0 and a+b>=c and b+c>=a and a+c>=b


def equilateral(sides):
    a, b, c = sides
    return triangle(a, b, c) and a == b and c == b and a == c


def isosceles(sides):
    a, b, c = sides
    return triangle(a, b, c) and (a == b or b == c or c == a)

def scalene(sides):
    a, b, c = sides
    return triangle(a, b, c) and a != b and b != c and c != a
